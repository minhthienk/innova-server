
from flask import Flask, request, send_file, abort, render_template
from common.dtc_converter import *


from flask import Blueprint
app_dtc_convert = Blueprint("app_dtc_convert", __name__)


@app_dtc_convert.route('/util/DTC Convert', methods=['GET', 'POST'])
def show_dtc_convert():

    a = '''
    <form action="" method="post">
    <input type="text" style="width:50%; padding: 5px 15px;" placeholder="Enter DTC" name="dtc-input" value="{{dtc_input}}">
    <input class="button_base button_input_submit" type="submit" name="submit_button" value="Convert To Hex">
</form>
'''
    b = '<p>hello</p>'
    if request.method == 'POST':
        if request.form['submit_button'] == 'Convert To Hex':
            dtc = request.form['dtc-input']
            return render_template(
                                  'dtc_convert.html',  
                                  dtc_input=dtc, 
                                  hex_input=dtc2hex(dtc))

        if request.form['submit_button'] == 'Convert To DTC':
            hexnum = request.form['hex-input']
            return render_template(
                                  'dtc_convert.html', 
                                  dtc_input=hex2dtc(hexnum), 
                                  hex_input=hexnum)

    elif request.method == 'GET':
        return render_template(
                              'dtc_convert.html', 
                              dtc_input='', 
                              hex_input='').format(a=a,b=b)


