import requests
import json
import pandas as pd

from pairs import un_pw

def get_api_data(query_text, results_size):
    
    patt_url = "https://api.ravelry.com/patterns/search.json?query="+query_text
    patt_resp = requests.get(patt_url, params={'page_size':results_size}, auth=(list(un_pw.keys())[0], list(un_pw.values())[0]))
    patts = pd.json_normalize(json.loads(patt_resp.text),'patterns')
    pattern_details_df = pd.DataFrame()
    for i in range(results_size):
        patt_id = str(patts['id'][i])
        patt_lookup = "https://api.ravelry.com/patterns/"+patt_id+".json"

        lookup_resp = requests.get(patt_lookup, auth=(list(un_pw.keys())[0], list(un_pw.values())[0]))
        patt_dets = pd.json_normalize(json.loads(lookup_resp.text))
        sub_df = patt_dets[['pattern.id', 'pattern.price', 'pattern.currency', 'pattern.projects_count', 'pattern.rating_average', 'pattern.rating_count', 'pattern.favorites_count', \
               'pattern.difficulty_average', 'pattern.difficulty_count']].copy()
        pattern_details_df = pattern_details_df.append(sub_df, ignore_index=True)

    df = pd.merge(patts[['id', 'name', 'designer.favorites_count','designer.knitting_pattern_count']], pattern_details_df, how='left', left_on='id', right_on='pattern.id')
    df.drop(['pattern.id'], axis=1, inplace=True)
    df.columns = ['id','name','designer_favorited','designer_pattern_count', 'price', 'currency', 'projects_count', 'rating_average', 'rating_count', \
                    'favorites_count','difficulty_average', 'difficulty_count']
    return df

def get_categories():
    cat_resp = requests.get("https://api.ravelry.com//pattern_categories/list.json")
    cat_1 = pd.json_normalize(json.loads(cat_resp.text)['pattern_categories'], 'children')[['id','name']]
    cat_1.columns = ['p.id','p.name']
    cat_2 = pd.json_normalize(json.loads(cat_resp.text)['pattern_categories']['children'], 'children',['name'], record_prefix="p.")[['p.id','p.name']]
    cat_3 = pd.json_normalize(json.loads(cat_resp.text)['pattern_categories']['children'], ['children','children'], record_prefix="p.")[['p.id','p.name']]
    categories = pd.concat([cat_1, cat_2, cat_3])
    cat_list = list(categories['p.name'])
    return cat_list


data = get_api_data("cowl", 10)

cat_list = get_categories()

import panel as pn
from bokeh.plotting import figure, show

pn.extension(loading_spinner='dots')



xaxis_input = pn.widgets.Select(options=list(data.columns), name='x-axis')
yaxis_input = pn.widgets.Select(options=list(data.columns), name='y-axis')


@pn.depends(xaxis_input, yaxis_input)
def plotchart(x_input, y_input):
    x = data[x_input]
    y = data[y_input]
    chart = figure(width=400, height=400)
    chart.circle(x,y, size=10, color='blue', alpha=0.5)
    return pn.panel(chart)


plot_interaction = pn.Column(xaxis_input, yaxis_input, plotchart)

search = pn.widgets.AutocompleteInput(name='Search', options=cat_list, restrict=False, case_sensitive=False)

result_count = pn.widgets.IntSlider(name='result size', start=1, end=100, step=1, value=10)



api_button = pn.widgets.Button(name='Run new search', button_type='primary')

def update(event):
    global data
    with pn.param.set_values(plot_interaction, loading=True):
        data = get_api_data(search.value, result_count.value)
    plot_interaction[2] = plotchart

api_button.on_click(update)

update_widgets = pn.Column("Update the data by making a new API call.  **Warning: this may take up to 90 seconds", \
                           pn.Row(search, result_count, api_button, height=100))

pn.template.FastListTemplate(title="Panel Demo", header_background = "#143250", 
                             main = [update_widgets, plot_interaction],
                             main_max_width='1500px',
                             accent_base_color='#1DC2BB').servable();