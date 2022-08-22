from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('Model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = float(request.form.get('Time'))
    data2 = float(request.form.get('v1'))
    data3 = float(request.form.get('v2'))
    data4 = float(request.form.get('v3'))
    data5 = float(request.form.get('v4'))
    data6 = float(request.form.get('v5'))
    data7 = float(request.form.get('v6'))
    data8 = float(request.form.get('v7'))
    data9 = float(request.form.get('v8'))
    data10 = float(request.form.get('v9'))
    data11 = float(request.form.get('v10'))
    data12 = float(request.form.get('v11'))
    data13= float(request.form.get('v12'))
    data14= float(request.form.get('v13'))
    data15= float(request.form.get('v14'))
    data16= float(request.form.get('v15'))
    data17= float(request.form.get('v16'))
    data18= float(request.form.get('v17'))
    data19= float(request.form.get('v18'))
    data20= float(request.form.get('v19'))
    data21= float(request.form.get('v20'))
    data22= float(request.form.get('v21'))
    data23= float(request.form.get('v22'))
    data24= float(request.form.get('v23'))
    data25 = float(request.form.get('v24'))
    data26= float(request.form.get('v25'))
    data27 = float(request.form.get('v26'))
    data28= float(request.form.get('v27'))
    data29= float(request.form.get('v28'))
    data30= float(request.form.get('Amount'))





    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9,data10, data11, data12, data13, data14,
                     data15, data16, data17,
                     data18, data19,data20,data21,data22, data23, data24, data25, data26, data27,data28,data29,data30]])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)