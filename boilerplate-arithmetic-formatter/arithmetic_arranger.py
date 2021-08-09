def arithmetic_arranger(problems, answer=False):
  arranged_problems = ""
  arranged_line = ["", "", ""]
  solutions = ""
  if len(problems) > 5:
    return "Error: Too many problems."
  for question in problems:
    text = question.split(" ")
    line_length = max(len(text[0]), len(text[2]))
    if not (text[1] in ["+", "-"]):
      return "Error: Operator must be '+' or '-'."
    if (len(text[0]) > 4 or len(text[2]) > 4):
      return "Error: Numbers cannot be more than four digits."
    if not (text[0].isdigit() and text[2].isdigit()):
      return "Error: Numbers must only contain digits."
      
    arranged_line[0] += " "  * (line_length-len(text[0])+2)
    # print(arranged_line[0])
    arranged_line[0] += text[0]
    arranged_line[1] += text[1] + " " * (line_length-len(text[2])+1) + text[2]
    arranged_line[2] += "-" * (line_length+2)
    if not question == problems[-1]:
        arranged_line[0] += "    "
        arranged_line[1] += "    "
        arranged_line[2] += "    "

    if answer == True:
      result = int(text[0]) + int(text[2]) if (text[1] == "+") else int(text[0]) - int(text[2])
      solutions += " " * (line_length-len(str(result))+2)
      solutions += str(result)
      if not question == problems[-1]:
        solutions += "    "
  arranged_problems = arranged_line[0] + "\n" + arranged_line[1] + "\n" + arranged_line[2]
  arranged_problems = arranged_problems + "\n" + solutions if (answer == True) else arranged_problems
  return arranged_problems
