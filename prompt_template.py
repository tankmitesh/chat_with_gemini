SUMMARY = """Give me summary of the context based on below instruction.
             First give short introduration summary based context.
             1. The primary goal is to provide a summary of the data without unnecessary repetition.
             2. Ensure the summary is approximately 40-50% of the original context length.
             3. In first section you should give little bit information about enitre context, what entire context said.
             4. Include key details such as incidents, dates, or topic-specific information.
             5. Explain each key points based in one or two lines.
             6. your points summary should be shuttle and stright.
             7. and third section give me full info about the conext summary, inclided summary of the bullet points.
             8. Focus on altering the grammar of the provided text.  
             9. Give last full summary of the data.       
             10. context mentioned any example / examples, explain in depth with seperate section and make sure you are
             using above points in the example and example explination clean and points wise.
             11. Make sure you are using words / text and sentence simple as possible.   
             context : {}"""



QUESTION = """can you guide and give me answer of this {}, can you also explain question answer in layman term."
            """



CODE_ANALYSIS = """Give me end to end analysis of the given code data as below.
                   Give all information with one line of explaintion and make sure you are mentioning why code required this change.
                   Do not make same format and section which i given to you, you can change it by yourself.

                   1. Interpretation :
                        - check each every variable names make sure variable is interpretation is moderate or high.
                        - class name / function name is hard to understand, suggest 2-3 names for the replacement.
                        - Give 2-3 variable suggestion for names.
                        - Check annotation / comments, if comments are not explain code lines properly then give me some
                          suggestions about comments.

                    2. Testing :    
                        - check any variables / package / function / class method / comments and unsed remove mentioned it.
                        - check mismatch data types and mistmatch flow in the code indicate with lines and variables names.
                        - give some suggestion about test validations.
                        - Give me average space and time complexity of the code.

                    3. Modification :
                        - If code do not have docstring, give suggestion of docstring, make sure docstring should be more clean, stright
                          with input / output data type, name default parameter, examples, raise different error, plot / image / file saving name
                    
                    4. Suggestions :
                        - Give me suggestion based on code.
                    
                    Check entire code line by line and give proper analysis.
                    CODE : {}"""

