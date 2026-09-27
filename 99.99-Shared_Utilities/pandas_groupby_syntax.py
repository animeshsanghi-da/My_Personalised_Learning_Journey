# ==============================================================================
# MASTER PANDAS GROUPBY & AGGREGATION SYNTAX BLUEPRINT
# ==============================================================================

# 1. FULL METHOD SIGNATURE & PARAMETER DEFINITIONS
DataFrame.groupby(
    by=None,             # Single col ('A'), list (['A','B']), Series, array, or level name
    axis=0,              # 0/'index' (rows). Note: axis=1 is deprecated in Pandas 2.0+
    level=None,          # Level name or int index when grouping a MultiIndex DataFrame
    as_index=True,       # True: group keys become index; False: flat SQL-style table
    sort=True,           # True: sorts group keys; False: keeps order of appearance (faster)
    group_keys=True,     # True: includes group keys in index when using .apply()
    observed=False,      # False: includes empty Categorical/pd.cut bins; True: keeps observed only
    dropna=True          # True: drops NaN group keys; False: treats NaN as a distinct group
)


# 2. COMPLETE OPERATIONAL CHAINING SYNTAX (All Patterns)

result_df = (
    df.groupby(
        by=['Cat_Col1', 'Cat_Col2'], # Single column string or list of columns
        as_index=False,              # False: SQL-style flat table; True: keys become index
        sort=False,                  # False: keeps original order (faster performance)
        observed=False,              # False: preserves empty pd.cut/qcut categories
        dropna=False                 # False: keeps NaN/null as a valid group label
    )
    
    # --------------------------------------------------------------------------
    # PATTERN A: COLUMN SELECTION (Optional)
    # --------------------------------------------------------------------------
    # ['Target_Col']                            # Select single column (Returns Series/DataFrame)
    # [['Col1', 'Col2']]                        # Select multiple columns
    
    # --------------------------------------------------------------------------
    # PATTERN B: AGGREGATION METHODS (Choose One)
    # --------------------------------------------------------------------------
    
    # B1. Single Built-in Aggregation
    ['Numeric_Col1'].count()
    # .sum() / .mean() / .median() / .count() / .min() / .max() / .std() / .nunique()

    # B2. Single Built-in Aggregation
    ['Numeric_Col1'].agg(['count', 'sum', 'max', 'min'])
    # .sum() / .mean() / .median() / .count() / .min() / .max() / .std() / .nunique()

    # B3. Dictionary Aggregation (Generates MultiIndex Headers)
    .agg({
        'Numeric_Col1': ['sum', 'mean', 'nunique', lambda x: round(x.mean() * 100, 2)],       # Multiple stats on one column
        'Numeric_Col2': 'max',                                                                # Single stat on column
        'Text_Col': 'count'                                                                   # Count non-null observations
    })
    
    # B4. Named Aggregation (RECOMMENDED: Clean & Flat Columns)
    .agg(
        total_value   = ('Numeric_Col1', 'sum'),
        average_value = ('Numeric_Col1', 'mean'),
        max_limit     = ('Numeric_Col2', 'max'),
        unique_counts = ('Text_Col', 'nunique'),
        custom_pct    = ('Numeric_Col1', lambda x: round(x.mean() * 100, 2)) # Custom Lambda
    )
    
    # --------------------------------------------------------------------------
    # PATTERN C: ADVANCED GROUP-LEVEL OPERATIONS (Alternative to .agg)
    # --------------------------------------------------------------------------
    
    # C1. Group Transformation (Broadcast Back to Original Rows)
    .transform(lambda x: x - x.mean())        # Broadcasts group stat back to original shape
    .transform('mean')

    # c2. Group Filtering (Filter DataFrame by Group Condition)
    .filter(lambda x: x['Numeric_Col1'].sum() > 1000) # Filters out entire groups by condition

    # C3. Custom Group Apply (Flexible Multi-Column / Complex Logic)
    .apply(custom_function)         # Applies custom function to each group DataFrame/Series
    
    # --------------------------------------------------------------------------
    # PATTERN D: INDEX CLEANUP
    # --------------------------------------------------------------------------
    .reset_index()                  # Flattens index if as_index=True was used
)