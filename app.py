from flask import Flask, render_template, url_for
import os
import json
app = Flask(__name__)


@app.route('/')
def index():
    values = {"value": 3.0}
    return render_template('index.html', context=values)


@app.route('/getDefault')
def getDefault():
    f = open('sample.json')
    data = json.load(f)
    print(data.keys())
    values = {"blade_length": data["actuator_activation_left"]
              ["blade_length"]["value"],
              "thin_bb_size_in_m": data["actuator_activation_left"]
              ["thin_bb_size_in_m"]["value"],
              "board_pattern": data["calibration"]
              ["board_pattern"]["value"],
              "board_square_size_in_cm": data["calibration"]
              ["board_square_size_in_cm"]["value"],
              "conf_threshold": data["cotton_detection_left1"]
              ["conf_threshold"]["value"],
              "distance_threshold": data["cotton_detection_left1"]
              ["distance_threshold"]["value"],
              "prediction_buffer_pix": data["cotton_tracking_left1"]
              ["prediction_buffer_pix"]["value"],
              "tracking_frames_length": data["cotton_tracking_left1"]
              ["tracking_frames_length"]["value"],
              "cd_error": data["detect_weed_left"]
              ["cd_error"]["value"],
              "ct_frames_to_consider": data["detect_weed_left"]
              ["ct_frames_to_consider"]["value"],
              "fd_frames_to_consider": data["detect_weed_left"]
              ["fd_frames_to_consider"]["value"],
              "se_error": data["detect_weed_left"]
              ["se_error"]["value"],
              "spraying_error": data["detect_weed_left"]
              ["spraying_error"]["value"],
              "ia_buffer": data["implement_actuation"]
              ["ia_buffer"]["value"],
              "max_implement_shift": data["implement_actuation"]
              ["max_implement_shift"]["value"],
              }
    return values


@app.route('/config')
def getconfig():
    f = open('sample.json')
    data = json.load(f)
    return data


if(__name__ == "__main__"):
    app.run(debug=True)
