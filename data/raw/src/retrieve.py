import pandas as pd


def simple_tokenize(text: str):
    """
    Convert text to lowercase and split into unique words (tokens).
    Returns a set to remove duplicates.
    """
    return set(text.lower().split())


def compute_overlap_score(text1: str, text2: str) -> int:
    """
    Compute similarity score based on word overlap.
    Counts how many unique words appear in both texts.
    """
    tokens1 = simple_tokenize(text1)
    tokens2 = simple_tokenize(text2)
    return len(tokens1.intersection(tokens2))


def retrieve_best_kb(transcript: str, kb_df: pd.DataFrame):
    """
    Find the best matching knowledge base document for a given transcript.
    
    Iterates through all KB rows and selects the one with the highest overlap score.
    
    Returns:
        best_doc_id (str or None)
        best_score (int)
    """
    best_score = 0
    best_doc = None

    for _, row in kb_df.iterrows():
        score = compute_overlap_score(transcript, row["content"])

        # Update best match if current score is higher
        if score > best_score:
            best_score = score
            best_doc = row

    # If no match found, return None
    if best_doc is None:
        return None, 0

    return best_doc["doc_id"], best_score


def match_calls_to_kb(calls_df: pd.DataFrame, kb_df: pd.DataFrame):
    """
    Match each call transcript to the most relevant KB document.
    
    For each call:
    - Compute best KB match
    - Store call_id, matched_doc_id, and score
    
    Returns:
        DataFrame with matching results
    """
    results = []

    for _, call in calls_df.iterrows():
        doc_id, score = retrieve_best_kb(call["transcript"], kb_df)

        results.append({
            "call_id": call["call_id"],
            "matched_doc_id": doc_id,
            "score": score
        })

    return pd.DataFrame(results)
