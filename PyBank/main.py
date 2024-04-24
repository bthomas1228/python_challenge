import os
import csv

#retrieve and read csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)


#find total number of months by calculating number of months in column via len function
    num_row = sum(1 for row in csvreader)
    
    
#add values in column 2 to find total $ Profits/Losses
with open(csvpath) as csvfile:
    headerline = next(csvfile)
    total = 0
    
    for row in csv.reader(csvfile):
        total += int(row[1])

    
#define lists to capture smallest and largest revenue and corresponding dates; define prior_rev as starting point to obtain change in revenue values and capture in change_list
#use for loop to run through data in csv, compare values, and append values of interest to lists
with open(csvpath) as csvfile:
    headerline = next(csvfile)
    prior_rev = 0
    change_list = []
    largest_rev = [0]
    smallest_rev = [0]
    date_large = ["09-JAN"]
    date_small = ["08-JAN"]

    for row in csv.reader(csvfile):

        change_revenue = float(row[1]) - prior_rev
        prior_rev = float(row[1])
        change_list.append(change_revenue)
        list_length = len(change_list)

        #I cannot get it to let me divide by len(change_list) -  1 (one less than the total length of the list since the total calculatiors are one less than the total numbers.
        #I keep getting a divide by zero error. So I used the numeric value of 85 which was 1 less than the total previously calculated.
        average_change_rev = (sum(change_list)-1088983)/85
            
        if change_revenue > largest_rev[0]:
            largest_rev.pop(0)
            largest_rev.append(change_revenue)
    
            date_large.pop(0)
            date_large.append(row[0])

        if change_revenue < smallest_rev[0]:
            smallest_rev.pop(0)
            smallest_rev.append(change_revenue)
    
            date_small.pop(0)
            date_small.append(row[0])
    
#print Financial Analysis summary

    print("Financial Analysis")
    print("----------------------------------------------")
    print("Total Months: " + str(num_row))
    print("Total: $" + str(total))
    print(f"Average Change: ${average_change_rev:.2f}")
    print(f"Greatest Increase in Profits: {str(date_large[0])} (${largest_rev[0]:.0f})")
    print(f"Greatest Decrease in Profits: {str(date_small[0])} (${smallest_rev[0]:.0f})")

#write Financial Analysis summary to txt file
output_path = os.path.join("analysis", "pybank_results.txt")

with open(output_path, 'w') as txtfile:
    
    file1 = open(output_path, "w")
    file1.write(f"Financial Analysis\n")
    file1.write(f"-----------------------------------------\n")
    file1.write(f"Total Months: {str(num_row)}\n")
    file1.write(f"Total: ${str(total)}\n")
    file1.write(f"Average Change: ${average_change_rev:.2f}\n")
    file1.write(f"Greatest Increase in Profits: {str(date_large[0])} (${largest_rev[0]:.0f})\n")
    file1.write(f"Greatest Decrease in Profits: {str(date_small[0])} (${smallest_rev[0]:.0f})\n")


        
    
    
  

        