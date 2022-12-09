#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#######################################
### Step 1 - Python Library Imports ###
#######################################

import dash
import dash_html_components as html
import pandas as pd
import dash_cytoscape as cyto

###################################################
### Step 2 - Persistent Local Variable Creation ###
###################################################

# Import Node and Edge Data - lets take a look
nodes_1 = pd.read_csv('../data/got-s1-nodes.csv', low_memory=False)
edges_1 = pd.read_csv('../data/got-s1-edges.csv', low_memory=False)

# Function to Create Graph
# Inputs - Node and Edge data
# Output - list of dictionaries
def create_cyto_graph(nodeData, edgeData):
    nodes_list = list()
    for i in range(len(nodeData)):
        node = {
                "data": {"id": nodeData.iloc[i,0], 
                         "label": nodeData.iloc[i,1]}
                
            }
        nodes_list.append(node)
    
    edges_list = list()
    for j in range(len(edges_1)):
        edge = {
                "data": {"source": edges_1.iloc[j,0], 
                         "target": edges_1.iloc[j,1],
                         "weight": edges_1.iloc[j,2]}
            }
        edges_list.append(edge)
    
    elements = nodes_list + edges_list
    return elements

# Assembling data for the 'elements' arguement
# Using the loaded CSV files and Func above
elements = create_cyto_graph(nodes_1, edges_1)

# Declare styleseet for Node and Edge Styling
default_stylesheet=[
            {'selector': 'node',
                'style': {
                        'width': '20',
                        'height': '20',
                        'background-color': 'blue',
                        'content': 'data(label)',
                        'font-size': '40px',
                        'text-outline-color': 'white',
                        'text-outline-opacity': '1',
                        'text-outline-width': '8px',
                    }
                },
            {'selector': 'edge',
                'style': {
                        'line-color': 'black'
                    }
                }
        ]

#####################################
### Step 3 - App. Initialisation ####
#####################################

# Initiaise 'app' and then server object
app = dash.Dash(__name__)
server = app.server

############################
### Step 4 - App. Layout ###
############################

app.layout = html.Div(children=[
                cyto.Cytoscape(
                    id='cyto-graph',
                    className='net-obj',
                    elements=elements,
                    style={'width':'80%', 'height':'600px'},
                    layout={'name': 'cose',
                            'padding': 200,
                            'nodeRepulsion': '7000',
                            'gravityRange': '6.0',
                            'nestingFactor': '0.8',
                            'edgeElasticity': '50',
                            'idealEdgeLength': '200',
                            'nodeDimensionsIncludeLabels': 'true',
                            'numIter': '6000',
                            },
                    stylesheet=default_stylesheet
                    )
                ])

### Step 5 is missed as no callbacks/ interactive features....

##################################
### Step 6 - App. Run Command ####
##################################

if __name__ == "__main__": #if app has been initialised then run the server
    app.run_server(debug=True)
    

##############
### Notes ####
##############

# - Until you stop the kernel you cannot run anything else.. (Ctrl + C 
#   or red stop)

# - If you do stop the kernel then the web-browser will start to 
#   dispaly error messages
    