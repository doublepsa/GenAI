from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import re


def _normalize_text(text: str) -> str:
    """
    Light normalization to reduce noise without destroying semantics.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


def compute_knowledge_score(reference: str, candidate: str) -> dict:
    """
    Computes a hybrid ROUGE + BLEU knowledge coverage score,
    tuned to be more forgiving for paraphrasing and concise summaries.

    Parameters
    ----------
    reference : str
        Ground-truth lecture summary (Slide.summary)
    candidate : str
        Student note summary (Note.summary)

    Returns
    -------
    dict
        {
            "rouge1": float,
            "rouge2": float,
            "rougeL": float,
            "bleu": float,
            "final_score": float
        }
    """

    if not reference or not candidate:
        return {
            "rouge1": 0.0,
            "rouge2": 0.0,
            "rougeL": 0.0,
            "bleu": 0.0,
            "final_score": 0.0
        }

    # Normalize texts
    ref_norm = _normalize_text(reference)
    cand_norm = _normalize_text(candidate)

    # Length statistics 
    ref_len = len(ref_norm.split())
    cand_len = len(cand_norm.split())
    length_ratio = min(cand_len / ref_len, 1.0) if ref_len > 0 else 0.0

    # ROUGE scoring
    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"],
        use_stemmer=True
    )

    rouge_scores = scorer.score(ref_norm, cand_norm)

    rouge1_f = rouge_scores["rouge1"].fmeasure
    rouge2_f = rouge_scores["rouge2"].fmeasure
    rougeL_f = rouge_scores["rougeL"].fmeasure

    # BLEU scoring
    smoothie = SmoothingFunction().method4
    bleu = sentence_bleu(
        [ref_norm.split()],
        cand_norm.split(),
        smoothing_function=smoothie
    )

    # Weighted base score paraphrase friendly
    final_score = (
        0.30 * rouge1_f +
        0.35 * rougeL_f +
        0.15 * rouge2_f +
        0.10 * bleu
    )

    # Prevents short but accurate summaries from being overly punished hopefully
    final_score *= (0.75 + 0.25 * length_ratio)

    # Semantic floor based on structural alignment
    # Prevents collapse when paraphrasing is strong
    semantic_floor = 0.15 * rougeL_f
    final_score = max(final_score, semantic_floor)

    return {
        "rouge1": round(rouge1_f, 4),
        "rouge2": round(rouge2_f, 4),
        "rougeL": round(rougeL_f, 4),
        "bleu": round(bleu, 4),
        "final_score": round(final_score * 100, 2)
    }
