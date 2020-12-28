from app import app
from app.utils.conf_parse import get_config
from app.utils.salty.sdc import handle_sbo_stream
from app.utils.sql import sql_queries
from flask import request, jsonify, redirect



@app.route('/')
@app.route('/home')
def root():
    return redirect('/api/v1/status', code=302)


@app.route('/api/v1/bouts')
def api_v1_bouts():
    bouts = sql_queries.select_all_bouts()
    
    if bouts:
        a = request.args.to_dict()
        b_list = []

        sort = a.get("sort")
        if sort:
            pass
        else:
            sort = "bout_date"

        num = a.get("num")
        if num:
            num = int(num)
        else:
            num = len(bouts)

        name = a.get("name")
        if name:
            for b in bouts:
                if name.upper() in b["red_fighter"].upper() or name.upper() in b["blue_fighter"].upper():
                    b_list.append(b)
        else:
            b_list = bouts

        sort_type = a.get("sort_type")
        if sort_type == "bottom":
            b_list = sorted(b_list, key=lambda i: i[f"{sort}"])
            b_list.reverse()
        else:
            b_list = sorted(b_list, key=lambda i: i[f"{sort}"])
        
        return jsonify(b_list[:num])

    return 'NO BOUTS'


@app.route('/api/v1/help')
def api_v1_help():
    help = {}
    help['/api/v1/bouts'] = 'Query the database and display bouts in json format.'
    help['/api/v1/help'] = 'Display avalible URLs and descriptions.'
    help['/api/v1/fighters'] = 'Query the database and display fighters in json format.'
    help['/api/v1/sbo'] = 'Salty Bout Observer URL to post current bout information.'
    help['/api/v1/status'] = 'Display config.txt information.'
    return jsonify(help)


@app.route('/api/v1/fighters')
def api_v1_fighters():
    fighters = sql_queries.select_all_fighters()
    
    if fighters:
        a = request.args.to_dict()
        f_list = []
        sort = a.get("sort")
        if sort:
            pass
        else:
            sort = "date_of_last_bout"

        num = a.get("num")
        if num:
            num = int(num)
        else:
            num = len(fighters)

        name = a.get("name")
        if name:
            for f in fighters:
                if name.upper() in f["name"].upper():
                    f_list.append(f)
        else:
            f_list = fighters

        sort_type = a.get("sort_type")
        if sort_type == "bottom":
            f_list = sorted(f_list, key=lambda i: i[f"{sort}"])
            f_list.reverse()
        else:
            f_list = sorted(f_list, key=lambda i: i[f"{sort}"])
        
        return jsonify(f_list[:num])

    return 'NO FIGHTERS'


@app.route('/api/v1/sbo', methods=['POST'])
def api_v1_sbo():
    sbo_stream = request.get_json()
    print('SBO STREAM:', sbo_stream)
    handle_sbo_stream(sbo_stream)
    return 'SBO STREAM'


@app.route('/api/v1/status')
def api_v1_status():
    conf = dict(get_config())
    conf["sql_secret"] = 'CHECK CONFIG'
    conf["sql_user"] = 'CHECK CONFIG'
    conf["is_running"] = True
    return jsonify(conf)
