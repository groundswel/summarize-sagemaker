#Some utilities to help prepare training data from csv files


def extract_substring(start_string_list, end_string_list, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Extracting 1st and 3rd field
            fields = line.strip().split(',')
            remaining_line = ','.join(fields[6:])
            for stringstart in [STRINGSTART_ARRAY]:
                try:
                    index = remaining_line.index(stringstart)
                    break
                except ValueError:
                    continue
            line = remaining_line[index:]
            
            # Initializing flag and substring
            found = False
            substring = ''
            
            # Converting line and start/end strings to lowercase
            line = line.lower()
            start_string_list = [start.lower() for start in start_string_list]
            end_string_list = [end.lower() for end in end_string_list]
            
            # Iterating through each start and end string
            for start in start_string_list:
                for end in end_string_list:
                    if start in line and end in line:
                        # Extracting substring between start and end
                        start_index = line.index(start) + len(start)
                        end_index = line.index(end)
                        substring = line[start_index:end_index].strip()
                        found = True
                        break
                if found:
                    break
            
            # If no match found, use the whole line
            if not found:
                substring = line
            
            # Printing the extracted substring
            print(f"{fields[0]}|{fields[1]}|{substring}")
            #print(f"{start},{end}")
  
  #Example:
  '''
  start_string_list = ["First section", "Another section start"]
  end_string_list = ["EOF","END","THE NEXT CHAPTER"]
  file_path = "file.csv"
  extract_substring(start_string_list,end_string_list,file_path)
  '''
  
  def split_string_after_nth_comma(s, n):
    # Split the string into a list on the comma delimiter
    string_list = s.split(',')
    
    # Check if the list has enough items
    if len(string_list) <= n:
        return ''
    
    # Return the remaining string
    return ','.join(string_list[n:])
  
 def get_substring(s, start, end):
    start_index = s.find(start)
    end_index = s.find(end)
    if start_index == -1 or end_index == -1:
        return ""
    else:
        return s[start_index+len(start):end_index]


 def parse_string_to_json(s):
    s = s.replace('"description":"', '')
    lines = s.split('\\n')
    out = {}
    for line in lines:
        key, val = line.split(':')
        out[key] = val
    return json.loads(json.dumps(out))
