import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree["type"] = "Inner"
    
    # Nodes that do not appear as a parent are leaves
    tree.loc[~tree["id"].isin(tree["p_id"]), "type"] = "Leaf"
    
    # Nodes without a parent are roots
    tree.loc[tree["p_id"].isna(), "type"] = "Root"
    
    return tree[["id", "type"]]