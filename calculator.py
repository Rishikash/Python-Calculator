from tkinter import *

first_num = second_num = operator =None

def get_oprator(op):
    global first_num,operator
    first_num = int(result_label['text'])
    operator = op
    result_label.config(text='')


def get_digit(digit):
    # print(digit)
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)


def clear():
    result_label.config(text='')

def get_result():
    global first_num, second_num, operator
    second_num = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_num + second_num))
    elif operator == '-':
        result_label.config(text=str(first_num - second_num))
    elif operator == '*':
        result_label.config(text=str(first_num * second_num))
    else:
        if second_num == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_num / second_num, 2))) 


root = Tk()

root.title('Python Calculater')
root.geometry("375x210")
root.resizable(False,False)
root.configure(background='#f0f0f0')

# result_label = Label(root, text='', bg='black', fg='white', anchor='center', padx=10, pady=20)
# result_label = Label(root, text='', bg='white', fg='black', anchor='center',padx=10, pady=20)
result_label = Label(root, text='', font=("Arial", 20), bd=10, bg='white', fg='black', padx=2, pady=2, width=20,relief="ridge", borderwidth=4, justify="right")
result_label.grid(row=0, column=0,columnspan=5, pady=9)

result_label.config(font=('verdana',13))

btn7 = Button(root,text='7', bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))
# btn7=Button(root, text='7', padx=20, pady=20, font=("Arial", 14), bg="#f0f0f0", command=lambda :get_digit(7))
# btn7.grid(row=0, column=0, sticky="nsew")


btn8=Button(root,text='8',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9=Button(root,text='9',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn_add=Button(root,text='+', bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_oprator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))

#second row

btn4=Button(root,text='4',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5=Button(root,text='5',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6=Button(root,text='6',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn_sub=Button(root,text='-',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_oprator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))

#third row

btn1=Button(root,text='1',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2=Button(root,text='2',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3=Button(root,text='3',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btn_mul=Button(root,text='*',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_oprator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))

#forth row

btnc=Button(root,text='C',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :clear())
btnc.grid(row=4,column=0)
btnc.config(font=('verdana',14))

btn0=Button(root,text='0',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btn_equal=Button(root,text='=',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_result())
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('verdana',14))

btn_div=Button(root,text='/',bg='#f0f0f0', font=("Arial", 5),fg='black',width=7, height=1,command=lambda :get_oprator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14))

root.mainloop()

