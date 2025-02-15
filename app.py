import streamlit as st
import matplotlib.pyplot as plt
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
st.set_page_config(page_title="Quiz",page_icon="https://static.vecteezy.com/system/resources/previews/017/349/652/non_2x/check-mark-and-cross-symbols-free-png.png")
st.title("Quiz")
st.markdown("""<style>
            .viewerBadge_link__qRIco {
                display: none;
            }
            a svg{
                display:none;
            }
            a{
                pointer:none;
                pointer-events: none;          
            }
            button.st-emotion-cache-iiif1v.ef3psqc4,header.st-emotion-cache-18ni7ap.ezrtsby2,button.st-emotion-cache-ztfqz8.ef3psqc5{
                display:none;
                pointer:none;
                pointer-events: none;  
            }
            span.st-emotion-cache-10trblm.e1nzilvr1{
                text-align:center;
            }
            .block-container.st-emotion-cache-1y4p8pa.ea3mdgi2{
                padding:0px;
                margin-left:16px;
                margin-bottom:10px;
            }
            .st-cg.st-da.st-ci.st-cj.st-ck.st-cl.st-cm.st-af.st-cn.st-co.st-cp.st-cq.st-cr.st-cs.st-bl.st-ct.st-cu.st-cv.st-ar.st-as {
                background-color: blue;
            }
            code.language-java {
                margin-right: 30px;
            }
            </style>""",True)
l=[]
# if not hasattr(st.session.state, 's'):
#     st.session.state.s = 0
l.append(datetime.now())
main=st.text_input("Enter Name*",placeholder="Enter your full name")
q1=st.radio("Q1 : What is the result of 5 * 3 + 2 / 9 ?",["1","2","15","16"],index=None,key="q1")
q2=st.radio("Q2 : What will be the result of 15%4",["3","1","5","12"],index=None,key="q2")
q3=st.radio("Q3 : Find the value of 2 to the power of 5 ",["10","25","3","32"],index=None,key="q3")
q4=st.radio("Q4 : Calculate the factorial of 4 ?",["16","20","24","28"],index=None,key="q4")
st.write("Q5 : What is the output of the following java code snippet ?")
st.code("int x = 5 ;\nSystem.out.println(x++);",language="java")
q5=st.radio("",["5","6","4","Error"],index=None,key="q5")
q6=st.radio("Q6 : Which keyword is used to define a class in Java ?",["class","Class","CLASS","cls"],index=None,key="q6")
q7=st.radio("Q7 : Which of the following is NOT a primitive data type in Java?",["int","double","String","boolean"],index=None,key="q7")
st.write("Q8 : What is the output of the following java code snippet ?")
st.code("int x = 10 ;\nint y = 5;\nSystem.out.println(x>y?'x is greater' : 'y is greater');",language="java")
q8=st.radio("",["x is greater","y is greater","10","5"],index=None,key="q8")
q9=st.radio("Q9 : In Java, Which keyword is used to define a method that can be accessed without creating an instance of the class ?",["static","public","void","private"],index=None,key="q9")
q10=st.radio("Q10 : Which of the following statements is true about Java packages ?",["A package can contain only one class","Package name should always be the same as the folder name","A package can be defined within another package","Packages cannot be imported in Java"],index=None,key="q10")
st.write("Q11 : What is the output of the following java code snippet ?")
st.code("String x = 'Hello' ;\nx.concat(' World');\nSystem.out.println(x);",language="java")
q11=st.radio("",["Hello","World","Hello World","null"],index=None,key="q11")
q12=st.radio("Q12 : Which of the following statements correctly declares a two-dimensional array in Java? ",["int [][] arr = new int[3,3]","int [][] arr = new int[3][3]","int [][] arr = new int[3]","int [] arr = new int[3]"],index=None,key="q12")
q13=st.radio("Q13 : What is the range of the char data type in Java? ",["-128 to 127","0 to 255","-32768 to 32767","-214783648 to 214783647"],index=None,key="q13")
q14=st.radio("Q14 : Which of the following in NOT a valid identifier in Java ? ",["my_variable","$variable","1variable","_variable"],index=None,key="q14")
q15=st.radio("Q15 : What is the default value of a local variable in Java ? ",["0","1","null","Depends on the data type"],index=None,key="q15")
st.write("Q16 : What is the output of the following java code snippet ?")
st.code("int x = 5 ;\nSystem.out.println(x ==5 && x<10);",language="java")
q16=st.radio("",["true","false","Error","True"],index=None,key="q16")
q17=st.radio("Q17 : What is size of the 'int' data type  in Java?",["4 bytes","2 bytes","8 bytes","1 bytes"],index=None,key="q17")
q18=st.radio("Q18 : Which data type in Java is used to store single-precision floating-point numbers? ",["float","double","char","int"],index=None,key="q18")
q19=st.radio("Q19 : What is the default value of the 'boolean' data type in Java? ",["null","false","0","true"],index=None,key="q19")
q20=st.radio("Q20 : Which data type in Java is used to store a single Unicode Character? ",["char","byte","short","int"],index=None,key="q20")
q21=st.radio("Q21 : What is the size of the 'double' data type in Java? ",["4 bytes","2 bytes","8 bytes","1 bytes"],index=None,key="q21")
q22=st.radio("Q22 : What is the range of the 'short' data type in Java? ",["-128 to 127","0 to 255","-32768 to 32767","-214783648 to 214783647"],index=None,key="q22")
q23=st.radio("Q23 : What is the default value of the 'byte' data type in Java? ",["0","1","null","false"],index=None,key="q23")
# if not hasattr(st.session.state, 'k'):
#     st.session.state.k = 0
# if(st.session.state.s!=st.session.state.k):
#             st.markdown("""<style>
#                         button.st-emotion-cache-7ym5gk.ef3psqc12 {
#                         display: none;
#                         }
#                         </style>""",True) 
#             st.session.state.s=st.session.state.k
if(st.button("Submit")):
    if(q1==None or q2==None or q3==None or q4==None or q5==None or q6==None or q7==None or q8==None or q9==None or q10==None or q11==None or q12==None or q13==None or q14==None or q15==None or q16==None or q17==None or q18==None or q19==None or q20==None or q21==None or q22==None or q23==None):
        st.warning("Attempt All Questions")
    elif(main==""):
        st.warning("Please enter your name")
    else:
        st.markdown("""<style>
            button.st-emotion-cache-7ym5gk.ef3psqc12 {
            display: none;
            }
            </style>""",True)
        # st.session.state.s+=1
        # if(st.session.state==st.session.state.k):
        #             st.session.state.k+=2
        l.append(datetime.now())
        marks={q1:"15",q2:"3",q3:"32",q4:"24",q5:"5",q6:"class",q7:"String",q8:"x is greater",q9:"static",q10:"A package can be defined within another package",q11:"Hello",q12:"int [][] arr = new int[3][3]",q13:"0 to 255",q14:"1variable",q15:"Depends on the data type",q16:"true",q17:"4 bytes",q18:"float",q19:"false",q20:"char",q21:"8 bytes",q22:"-32768 to 32767",q23:"0"}
        count=0
        find_index=0
        wrong_answer={}
        right_answer={}
        for key,value in marks.items():
            find_index+=1
            if(key==value):
                count+=1
            else:
                wrong_answer[find_index]=key
                right_answer[find_index]=value
        try:
            # Load credentials from environment variable
            json_creds = os.getenv('USERDATASTORE_JSON')
            if json_creds is None:
                raise ValueError("USERDATASTORE_JSON environment variable is not set")
            creds_dict = json.loads(json_creds)
            scope=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            cre=ServiceAccountCredentials.from_json_keyfile_name(creds_dict,scope)
            client=gspread.authorize(cre)
            spreadsheet = client.open('quiz')
            spreadsheet.share('deepanshuantil4113@gmail.com', perm_type='user', role='writer')
            worksheet = spreadsheet.get_worksheet(0) 
            last_row_index = len(worksheet.col_values(1)) + 1 
            l_key=[]
            l_value=[]
            column_a_values = worksheet.col_values(1)
            column_b_values = worksheet.col_values(2)
            for x in column_a_values:
                if(x!="Name"):
                    l_key.append(x)
            for y in column_b_values:
                if(y!="Marks"):
                    l_value.append(int(y))
            c=0
            l_key.append(main)
            l_value.append(count)
            n = len(l_key)
            for i in range(n):
                for j in range(0, n-i-1):
                    if l_value[j] < l_value[j+1]:
                        l_value[j], l_value[j+1] = l_value[j+1], l_value[j]
                        l_key[j], l_key[j+1] = l_key[j+1], l_key[j]
            print(l_key)
            print(l_value)
            for x in range(len(l_key)):
                c+=1
                if(count==l_value[x] and main==l_key[x]):
                    break
            st.write("Your rank : " + str(c))
            row_data = [str(main), str(count),'23',str(l[0]),str(l[1]),str(l[1]-l[0]),c,str(wrong_answer),str(right_answer)]  
            print(row_data)
            worksheet.append_row(row_data, value_input_option='RAW', insert_data_option='INSERT_ROWS', table_range=f"A{last_row_index}")
            st.write("Your Score is : " + str(count) + "/ 23") 
            st.write("Your Score " + str(float((count/23) *100))+ "%")
            a1=st.expander("Answer 1")
            a1.code("class A {\n\tpublic static void main(String[] args) {\n\t\tint a = (5 * 3) + (2 / 9); // using BODMAS formula first 2 / 9 ,second 5*3 and then 15+0\n\t\tSystem.out.println('Result of 5 * 3 + 2 / 9 : ' +a);\n\t}\n}\n// output:-\n// 15",language="java")
            a2=st.expander("Answer 2")
            a2.code("class A {\n\tpublic static void main(String[] args) {\n\t\tint a = 15 % 4; // % means show remainder , so 15%4 is 3\n\t\tSystem.out.println('Result of 15%4 : ' + a);\n\t}\n}\n// output:-\n// 3",language="java")
            a3=st.expander("Answer 3")
            a3.code("import java.lang.Math;\nclass A {\n\tpublic static void main(String[] args) {\n\t\tdouble a= Math.pow(2, 5); // 2 to the power of 5 is 2*2*2*2*2\n\t\tSystem.out.println('2 to the power of 5 : ' + a);\n\t}\n}\n// output:-\n// 32",language="java")
            a4=st.expander("Answer 4")
            a4.code("class A {\n\tpublic static void main(String[] args) {\n\t\tint fact = 1; // start multiply by 1\n\t\tfor (int i = 2; i <= 4; i++) { // start by 2 because 1 *1 is 1 thatwhy start by 2 \n\t\t\tfact *= i; // fact value change by fact * by i for ex:- fact is 1 so fact * 2 is 2 then fact is 2  so 2*3 fact is 6 so on...\n\t\t}\n\t\tSystem.out.println('Factorial of 4 : '+ fact);\n\t}\n}\n// output:-\n// 24",language="java")
            a5=st.expander("Answer 5")
            a5.code("class A {\n\tpublic static void main(String[] args) {\n\t\tint x = 5 ;\n\t\tSystem.out.println(x++);// first x value is 5 and then after increment so after print x value is 6\n\t}\n}\n// output:-\n// 5",language="java")
            a8=st.expander("Answer 8")
            a8.code("class A {\n\tpublic static void main(String[] args) {\n\t\tint x = 10 ;\n\t\tint y = 5;\n\t\tSystem.out.println(x>y?'x is greater' : 'y is greater'); // x>y if condition true return x is greater else y is greater\n\t}\n}\n// output:-\n// x is greater",language="java")
            a12=st.expander("Answer 12")
            a12.code("class A {\n\tpublic static void main(String[] args) {\n\t\tString x = 'Hello' ;\n\t\tx.concat(' World'); // x concat (' world') but not save if x=x.concat(' world'); then concat with value of x \n\t\tSystem.out.println(x);\n\t}\n}\n// output:-\n// Hello",language="java")
            a13=st.expander("Answer 13")
            a13.code("class A {\n\tpublic static void main(String[] args) {\n\t\tint [][] arr = new int[3][3]// to declare 2d array which include default value 0  it create a matrix 3*3",language="java")
            a16=st.expander("Answer 16")
            a16.code("class A {\n\tpublic static void main(String[] args) {\n\t\tint x = 5 ;\n\t\tSystem.out.println(x ==5 && x<10);// it check both condition if condition is true then print true otherwise print false it check x is equal to 5 and x is less than 10\n\t}\n}\n// output:-\n// true",language="java")
            a19=st.expander("Answer 19")
            a19.code("class A {\n\tstatic boolean myBoolean;\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println('Default value of boolean: '' + myBoolean);//default value of boolean always is flase \n\t}\n}\n// output:-\n// false",language="java")
            a23=st.expander("Answer 23")
            a23.code("class A {\n\tpublic static void main(String[] args) {\n\t\tbyte myByte;\n\t\tSystem.out.println('Default value of byte: ' + myByte);// default value of byte is 0\n\t}\n}\n// output:-\n// 15",language="java")
            
            st.set_option('deprecation.showPyplotGlobalUse', False)
            try:
                person=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
                grouped_values = {}
                for i, x in enumerate(person):
                            if i < len(l_value): 
                                if x not in grouped_values:
                                    grouped_values[x] = []
                                grouped_values[x].append(l_value[i])
                for x, y_values in grouped_values.items():
                    plt.scatter([x] * len(y_values), y_values,label="Total marks : 23")
                plt.title('Results')
                plt.legend(["Total marks : 23"])
                st.pyplot()
            except Exception as e:
                st.error(e)
        except Exception as e:
            st.error("Error : " + str(e))
