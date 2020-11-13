import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import views.real_time.real_time_callbacks
#from views.trends.const import year_options
#from components.select.select_component import new_select
import pandas as pd
import dash_table



layout = html.Div(
			
[
        dbc.Row(
			dbc.Col(
				html.H3("Considering the desired product characteristics of the gelatin such as Bloom, Viscosity and Clarity, this tab will display the associated parameters with higher probability of producing gelatin with those desired characteristics"), 
				width={"size": 8}
				), justify = "center"
			),
			#html.Br(),
			html.Br(),
		dbc.Row(
            [ 
				dbc.Col([
					dbc.Card([
                        dbc.CardHeader(
							html.P("1. Enter desired values for Bloom, Viscosity and Clarity",className='secondary-title')),
						dbc.CardBody([
					html.P(["Input Bloom",html.Br(), "Range [175-300]"]),
					dbc.Input(type="number", min=175, value = 250, max=300, step=1, id="desired_bloom"),
					html.Br(),
					
					html.P(["Input Viscosity",html.Br(), "Range [27-52]"]),
					dbc.Input(type="number", min=27, value = 40, max=52, step=1, id="desired_viscosidad"),
					html.Br(),
					
					html.P(["Input Clarity", html.Br(),"Range [23-78]"]),
					dbc.Input(type="number", min=23, value = 45, max=78, step=1, id="desired_claridad"),
					html.Br(),
					
					dbc.Button("Calculate", id="knn_trigger_button",color="primary", className="mr-1", n_clicks=0)
						]

						)]),
                ], 
				width={"size": 2,"offset": 1}, align = "start"
				),
				
				dbc.Col(
					[
						dbc.Card([
                        dbc.CardHeader(html.P("2. Process variables measurements that would produce similar levels of Bloom, Viscosity and Clarity as entered in 1.",className='secondary-title')),
						dbc.CardBody(
						dash_table.DataTable(id="knn_table", columns = [], data = [],style_cell={'textAlign': 'center', 'font-family':'verdana'})#, style_table={'overflowX': 'auto'})
						)]),

					], width={"size": 4}, align = "start"
					),
				
				dbc.Col(
					[
						dbc.Card([
							dbc.CardHeader(html.P("3. Using the process variable measurements found, this will be the expected Bloom, Viscosity and Clarity levels",className='secondary-title')),
							dbc.CardBody(dash_table.DataTable(id="knn_table_pred", columns = [], data = [],style_cell={'textAlign': 'center', 'font-family':'verdana'}))#, style_table={'overflowX': 'auto'}))
						])
					], width={"size": 4}, align = "start"
					)
						
            ], align = "center"
        ),
		
		#dbc.Row(
		#	[
		#		dbc.Col(
		#		dash_table.DataTable(id="knn_table", columns = [], data = [], style_table={'overflowX': 'auto'}),
		#		width={"size": 10, "offset": 1}
		#		)
		#	]
		#)
    ],
    className='ccontainer'
)

