import streamlit as st
import joblib
import sklearn as sk
st.title('Student Dropout Prediction')
# Marital status,Application mode,Application order,Course,Daytime/evening attendance,Previous qualification,
# Nacionality,Mother's qualification,Father's qualification,Mother's occupation,Father's occupation,Displaced,Educational special needs,Debtor,Tuition fees up to date,Gender,Scholarship holder,Age at enrollment,International,Curricular units 1st sem (credited),Curricular units 1st sem (enrolled),Curricular units 1st sem (evaluations),Curricular units 1st sem (approved),Curricular units 1st sem (grade),Curricular units 1st sem (without evaluations),Curricular units 2nd sem (credited),Curricular units 2nd sem (enrolled),Curricular units 2nd sem (evaluations),Curricular units 2nd sem (approved),Curricular units 2nd sem (grade),Curricular units 2nd sem (without evaluations),Unemployment rate,Inflation rate,GDP,Target
# 1,8,3,11,1,1,1,22,14,6,6,1,0,0,1,0,0,19,0,0,6,8,4,11.25,0,0,6,8,4,12.0,0,10.8,1.4,1.74,Enrolled
# 1,4,1,17,0,3,1,3,14,3,4,0,0,0,1,0,0,28,0,0,5,7,5,13.714285714285714,0,0,5,7,5,13.142857142857142,0,16.2,0.3,-0.92,Graduate

model = joblib.load('del.joblib')
x = [1,4,1,17,0,3,1,3,14,3,4,0,0,0,1,0,0,28,0,0,5,7,5,13.714285714285714,0,0,5,7,5,13.142857142857142,0,16.2,0.3,-0.92]
# test1 = st.text_input("Marital status", value = "")
# test2 = st.text_input("attendance", value = "")
# test3 = st.text_input("Previous qualification", value = "")
# test4 = st.text_input("Nationality", value = "")
# test5 = st.text_input("Mother's qualification", value = "")
# test6 = st.text_input("Father's qualification", value = "")
# test7 = st.text_input("Mother's occupation", value = "")
# test8 = st.text_input("Displaced", value = "")
# test9 = st.text_input("Special Needs", value = "")
# test10 = st.text_input("Debtor", value = "")
# test11 = st.text_input("Tuition fees up to date", value = "")
# test12 = st.text_input("Gender", value = "")
# test13 = st.text_input("Scholarship holder", value = "")
# lst = [test1,0,0,0,test2,test3,test4,test5,test6,3,4,0,0,0,1,0,0,28,0,0,5,7,5,13.714285714285714,0,0,5,7,5,13.142857142857142,0,16.2,0.3,-0.92,1]
st.write(model.predict(x))