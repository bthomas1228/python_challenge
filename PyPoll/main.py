import os
import csv

#retrieve and read csv file
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
    
#define lists to capture specific data sets for further analysis
    total_list = []
    Candidate_list = []
                                         
#load Candidate data into total_list for analysis via loop
    for row in csv_reader:
        total_list.append(row[2])
        
#loop through list to compare each row to the Candidate_list contents to see if new candidate is found; if yes, add to list via append function
     
        if row[2] not in Candidate_list:
            Candidate_list.append(row[2])          
              
#define variables to represent the unique candidates
         
    candidate1 = Candidate_list[0]
    candidate2 = Candidate_list[1]
    candidate3 = Candidate_list[2]

#find the total number of votes using the len (length) function   
    total_votes=len(total_list)

#define variables to keep track of voter counts for each of the unique candidates, set to 0 to start
    total_count1 = 0
    total_count2 = 0
    total_count3 = 0

#loop through candidates in the total_list to count votes per candidate, store as total_count
    for candidate in total_list:
        if candidate == candidate1:
            total_count1 = total_count1 + 1
        elif candidate == candidate2:
            total_count2 = total_count2 + 1
        elif candidate == candidate3:
            total_count3 = total_count3 + 1

#calculate percentage of total votes for each unique candidate using previously defined variables
    perc1 = total_count1 / total_votes
    perc2 = total_count2 / total_votes
    perc3 = total_count3 / total_votes

    
#print results; for "winner" used conditional to compare total votes and print the candidate that had the most total_count votes

    print("Election Results")
    print("--------------------------")
    print("Total Votes: " +str(total_votes))
    print("--------------------------")
    print(str(candidate1) + ": " +str("{:.2%}".format(perc1)) + " (" + str(total_count1) + ")")
    print(str(candidate2) + ": " +str("{:.2%}".format(perc2)) + " (" + str(total_count2) + ")")
    print(str(candidate3) + ": " +str("{:.2%}".format(perc3)) + " (" + str(total_count3) + ")") 
    print("--------------------------")


    if total_count1 > total_count2 and total_count1 > total_count3:
        print("Winner: " + str(candidate1))

    elif total_count2 > total_count1 and total_count2 > total_count3:
        print("Winner: " + str(candidate2))

    elif total_count3 > total_count2 and total_count3 > total_count1:
        print("Winner: " + str(candidate3))

#write results to text file and store in Analysis folder

output_path = os.path.join("analysis", "pypoll_results.txt")

with open(output_path, 'w') as txtfile:
    
    file1 = open(output_path, "w")
    file1.write(f"Election Results\n")
    file1.write(f"--------------------------\n")
    file1.write(f"Total Votes: {str(total_votes)}\n")
    file1.write(f"--------------------------\n")
    file1.write(f"{candidate1}: {perc1:.2%} ({str(total_count1)})\n")
    file1.write(f"{candidate2}: {perc2:.2%} ({str(total_count2)})\n")
    file1.write(f"{candidate3}: {perc3:.2%} ({str(total_count3)})\n") 
    file1.write(f"--------------------------\n")
    file1.write(f"Winner: {str(candidate2)}\n")



    

  


        
 





                


  
        
# do function for each candidate
#get num_votes from above for loop

           

            
  
  

                                                                                                                                                      

   
       



        




    
   
            

    
    
    
    
    
    
    
    
