import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Use .shape to get the dimensions of the DataFrame
    rows, cols = players.shape
    return [rows, cols]