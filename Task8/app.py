import random  
import string  

from flask import Flask,request,render_template

app = Flask(__name__)

###################################################


def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  


lst = []
lst1 = []

@app.route('/',methods=['GET','POST'])
def short_url():
    if request.method=='GET':
        return render_template('shorten_url.html')
    else:
        url = request.form.get('url')
        if(len(url)!=0):
            num1 = random.randint(5,9)
            num2 = random.randint(2,5)
            s = random_string(num1,num2)
            # while(s in lst1):
            #     s = random_string(num1,num2)
            final_url = "http://127.0.0.1:5000/"+s
            lst.append(url) 
            lst1.append(final_url)
            return render_template('shorten_url.html',url1 = url,url2=final_url)
        else:
            return render_template('shorten_url.html',url1 = "",url2="")
        
@app.route('/history')
def history():
    s1 = zip(lst,lst1)
    return render_template('history.html',s1=s1)

###################################################

if __name__ == '__main__':
    app.run(debug=True)