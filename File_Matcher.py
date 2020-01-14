import fnmatch
import os

def list_files():
    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files: ", file)

        if fnmatch.fnmatch(file, "*.rb"):
            print("Ruby files: ", file)

        if fnmatch.fnmatch(file, "*.yml"):
            print("Yaml files: ", file)

        if fnmatch.fnmatch(file, "*.py"):
            print("Python files: ", file)


list_files()
    

Python files:  Access_Portions_Strings.py
Python files:  Adding_List_Elements.py
Python files:  Assignment_Operators.py
Python files:  Change_Variable_Values.py
Python files:  Check_String_Character_Type.py
Python files:  Comments.py
Python files:  Conditionals.py
Python files:  Conditionals_Compound.py
Python files:  Conditional_Operators_List.py
Python files:  Cond_Comp_Prac.py
Yaml files:  Config.yml
Python files:  Convert_Int_Float_Dec_Complex.py
Python files:  custom_generator.py
Python files:  custom_iterator_class.py
Python files:  Data-Types.py
Python files:  Decimal_VS_Float.py
Python files:  Del_Dict_Items.py
Python files:  Dictionary_View_Objects.py
Python files:  dunder_init.py
Python files:  dunder_repr.py
Python files:  Dynamic_Reducer.py
Python files:  File_Builder.py
Python files:  File_Matcher.py
Python files:  Finding_Substring_Find_Index_In.py
Python files:  Find_Replace_Str_Values.py
Python files:  Functions_Return_Values_From.py
Python files:  Function_All_Args.py
Python files:  Function_Arg_Unpacking.py
Python files:  Function_Default_Args.py
Python files:  Function_Keyword_Args.py
Python files:  Function_Named_Args.py
Python files:  Function_Nesting.py
Python files:  Function_Syntax.py
Python files:  Get_Function_Dictionary.py
Python files:  helper.py
Python files:  Heredoc.py
Python files:  Histogram_Practice.py
Python files:  Histogram_Project.py
Python files:  HTML_Heading_Generator_Function.py
Python files:  Incrementing-Matrix-Function.py
Python files:  Index_Based_Str_Interpolation.py
Python files:  Inheritance.py
Python files:  Join_Function.py
Python files:  Lambdas.py
Python files:  Lambda_Practice.py
Python files:  Lists.py
Python files:  Lists_Adv_Ranges_Slices.py
Python files:  Lists_Nested_Dictionaries.py
Python files:  List_Comprehension.py
Python files:  List_Query_Processes.py
Python files:  List_Ranges.py
Python files:  List_Ranges_Practice.py
Python files:  List_Sort.py
Text files:  logger.txt
Python files:  Loops_Basics.py
Python files:  Loops_Comb_Flat_Lists.py
Python files:  Loops_Cont_Break.py
Python files:  Loops_While.py
Python files:  Loop_Ranges.py
Python files:  Loop_Through_Strings.py
Python files:  main.py
Python files:  Manual_Exponent_Function.py
Python files:  math_Functions.py
Python files:  Math_Ops.py
Python files:  MDT_Nested_Lists.py
Python files:  Median_Odd_No_List.py
Python files:  Neg_Index_String.py
Python files:  Nested_Coll_Dictionaries.py
Python files:  New_Key_Value_Pairs_Dictionary.py
Python files:  Num_Types.py
Python files:  Partition_Function.py
Python files:  PEMDAS.py
Python files:  Polymorphic_Function.py
Python files:  Polymorphism_HTML_Generator.py
Python files:  Popular_Math_Functions.py
Python files:  Project_Fizz_Buzz.py
Python files:  Python_Dictionaries.py
Python files:  Python_Operator_Library.py
Python files:  Raw_Multiline_String.py
Python files:  Reassign_Elements_to_Tuples.py
Python files:  Reduce_Practice.py
Python files:  Remove_First_Last_List.py
Python files:  Remove_List_Elements.py
Ruby files:  scripts.rb
Python files:  Set_Data_Structure.py
Python files:  Set_Merging.py
Text files:  Something.txt
Text files:  Something2.txt
Python files:  Sorted_Function.py
Python files:  Split_Function.py
Python files:  Store_Slices_Class.py
Python files:  String_Basics.py
Python files:  String_Case_Functions.py
Python files:  String_Interpolation.py
Python files:  String_Interpolation_Practice.py
Python files:  Strip_LStrip_Rstrip.py
Python files:  Ternary_Operator.py
Python files:  Tuples.py
Python files:  Tuples_Nested_Lists.py
Python files:  Tuple_Dict_Key.py
Python files:  Tuple_Remove_Elements.py
Python files:  Tuple_Slices.py
Python files:  Tuple_Zip_Function.py
Python files:  Value_String_List.py
Python files:  Variables.py
Python files:  Web_Scraper_Project.py
Python files:  Weighted_Lottery_Function.py