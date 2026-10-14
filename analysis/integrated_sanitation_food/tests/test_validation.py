"""Synthetic checks for the address-year counting logic (no external dataset needed)."""
import pandas as pd


def test_one_to_one_aggregated_join_does_not_multiply_rows():
    sanitation = pd.DataFrame({"Address Key": ["10 MAIN ST"] * 3, "Year": [2025] * 3, "ID": [1, 2, 3]})
    food = pd.DataFrame({"Address Key": ["10 MAIN ST"] * 4 + ["11 MAIN ST"],
                         "Year": [2025] * 5, "ID": [11, 12, 13, 14, 15]})
    left = sanitation.groupby(["Address Key", "Year"], as_index=False).agg(Complaints=("ID", "size"))
    right = food.groupby(["Address Key", "Year"], as_index=False).agg(Inspections=("ID", "size"))
    joined = right.merge(left, how="left", on=["Address Key", "Year"], validate="one_to_one")
    assert len(joined) == 2
    assert joined["Inspections"].sum() == 5
    assert joined["Complaints"].sum() == 3
    assert pd.isna(joined.loc[joined["Address Key"] == "11 MAIN ST", "Complaints"].iloc[0])


def test_dates_not_string_year():
    dates = pd.to_datetime(pd.Series(["2025-01-02", "bad"]), errors="coerce", format="mixed")
    assert dates.dt.year.astype("Int64").tolist()[0] == 2025
    assert dates.isna().sum() == 1


def test_address_parenthetical_normalization():
    import pandas as pd
    import re
    def key(series):
        a=series.astype('string').str.upper().str.strip()
        return (a.str.replace(r'\([^)]*\)',' ',regex=True)
                 .str.replace(r'[.,]',' ',regex=True)
                 .str.replace(r'\s+',' ',regex=True).str.strip())
    assert key(pd.Series([' 5024 S Wolcott (1900W) ', '5024 S WOLCOTT'])).nunique()==1


def test_ungraded_outcomes_excluded_from_failure_denominator():
    results=pd.Series(['Fail','Pass','Pass w/ Conditions','No Entry','Not Ready'])
    cats=results.astype('string').str.upper()
    graded=cats.isin(['FAIL','PASS','PASS W/ CONDITIONS'])
    failed=cats.eq('FAIL')
    assert graded.sum()==3 and failed.sum()==1
