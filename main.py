from flask import Flask
import numpy
app=Flask(__name__)

a,b,c,d,e=map(int,input().split())
mas = [a,b,c,d,e]
lst_number = [x for x in mas if x < 0]
result = numpy.prod(lst_number)

if __name__ == '__main__':
    app.run(debug=True)