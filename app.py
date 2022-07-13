from flask import Flask, render_template, url_for, request, redirect
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
              "cotton_pixelcells_threshold": data["sprayer_activation_node_left"]
              ["cotton_pixelcells_threshold"]["value"],
              "distance_between_nozzles": data["sprayer_activation_node_left"]
              ["distance_between_nozzles"]["value"],
              "minimum_sprayer_delay": data["sprayer_activation_node_left"]
              ["minimum_sprayer_delay"]["value"],
              "pipeline_time": data["sprayer_activation_node_left"]
              ["pipeline_time"]["value"],
              "slip_time": data["sprayer_activation_node_left"]
              ["slip_time"]["value"],
              "speed_worldcoordinates": data["sprayer_activation_node_left"]
              ["speed_worldcoordinates"]["value"],
              "ttf_sa_time": data["sprayer_activation_node_left"]
              ["ttf_sa_time"]["value"],
              "weed_pixelcells_threshold": data["sprayer_activation_node_left"]
              ["weed_pixelcells_threshold"]["value"],

              }
    return values


@app.route('/config', methods=['POST', 'GET'])
def handle():
    if(request.method == 'GET'):
        try:
            f = open('sample2.json')
            data = json.load(f)
        except:
            f = open('sample.json')
            data = json.load(f)
    else:
        api_data = request.json
        c = 0
        f = open('sample.json')
        data = json.load(f)
        for i in data:
            t1 = data[i]  # dictionary
            for j in t1:
                t1[j]['value'] = float(api_data[c]['value'])
                c += 1
        json_object = json.dumps(data)
        with open("sample2.json", "w") as outfile:
            outfile.write(json_object)
    return data


if(__name__ == "__main__"):
    app.run(debug=True)
