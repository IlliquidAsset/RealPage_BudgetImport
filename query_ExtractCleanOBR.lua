let
    Source = Excel.Workbook(
        File.Contents("C:\Users\volprop\Volunteer Properties\Finance Team - Documents\2025 Budgets\2. Ready for Owner Review\2025 Budget 18Thirty TN243 Owner 2024.12.06.xlsm"),
        null,
        true
    ),
    OwnerBudgetReport_Sheet = Source{[Item="Owner Budget Report",Kind="Sheet"]}[Data],
    A1Value = OwnerBudgetReport_Sheet{0}[Column1],

    // Remove top headers
    #"Removed Top Rows" = Table.Skip(OwnerBudgetReport_Sheet, 2),

    // Remove completely blank rows
    #"Removed Blank Rows" = Table.SelectRows(#"Removed Top Rows", each 
        not List.IsEmpty(List.RemoveMatchingItems(Record.FieldValues(_), {"", null}))
    ),

    // Remove unwanted columns after Owner Notes
    #"Removed Columns" = Table.RemoveColumns(#"Removed Blank Rows",
        {"Column19", "Column22", "Column23", "Column24", "Column25", "Column26", "Column27",
         "Column28", "Column29", "Column30", "Column31", "Column32", "Column33", "Column34",
         "Column35", "Column36", "Column37", "Column38", "Column39", "Column40", "Column41",
         "Column42", "Column43", "Column44", "Column45"}),

    // Promote headers
    #"Promoted Headers" = Table.PromoteHeaders(#"Removed Columns", [PromoteAllScalars=true]),

    // Change column types
    #"Changed Type" = Table.TransformColumnTypes(
        #"Promoted Headers",
        {
            {"Column1", type text},
            {"1/31/2025", type number}, {"2/28/2025", type number}, {"3/31/2025", type number}, {"4/30/2025", type number}, 
            {"5/31/2025", type number}, {"6/30/2025", type number}, {"7/31/2025", type number}, {"8/31/2025", type number}, 
            {"9/30/2025", type number}, {"10/31/2025", type number}, {"11/30/2025", type number}, {"12/31/2025", type number}, 
            {"Total", type number}, {"Projection", type number}, {"$∆ (b/w)", type number}, {"%∆", type number}, 
            {"$/Unit", type number}, {"VP Notes", Int64.Type}, {"Owner Notes", type any}
        }
    ),

    // Remove rows where Column1 is blank or null
    #"Remove Blank Column1" = Table.SelectRows(#"Changed Type", each 
        [Column1] <> null and Text.Trim([Column1]) <> ""
    ),

    // Add the A1 value as Location_ID
    #"Add Location_ID" = Table.AddColumn(#"Remove Blank Column1", "Location_ID", each A1Value)
in
    #"Add Location_ID"