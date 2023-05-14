# zoom-attendance
Zoom attendance duration aggregator in python

Provide the correct path and set the maximum duration of your classes in the main setup, and then run the file.

    path = "zoom_attn/"
    pattern = "*.csv"
    max_duration = 75 # maximum duration per class
    rowskip = 1 # first row in zoom csv files has column header data

Change the value from 0 to 1 if you want to print the dates for the files you are processing (sanity check to ensure no double-counts)
    
    att_dict = compute_attn(path, pattern, max_duration, rowskip, 0)
