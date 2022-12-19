from economic_data.config import fred, pd, px, plt
import time

def unemployee_rate():
    unrate = fred.get_series(series_id='UNRATE')
    unrate.plot(figsize=(10, 5), title='Unemployment Rate', lw=2)
    plt.show()
    
def unemployee_line_chart():
    unemp_df = fred.search('unemployment rate state', filter=('frequency','Monthly'))
    unemp_df = unemp_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')
    unemp_df = unemp_df.loc[unemp_df['title'].str.contains('Unemployment Rate')]
    all_results = []

    for myid in unemp_df.index:
        print("unemp_df.index: ", myid)
        results = fred.get_series(myid)
        results = results.to_frame(name=myid)
        all_results.append(results)
        time.sleep(0.1) # Don't request to fast and get blocked
    uemp_results = pd.concat(all_results, axis=1)

    cols_to_drop = []
    for i in uemp_results:
        print("uemp_result: ", i)
        if len(i) > 4:
            cols_to_drop.append(i)
    uemp_results = uemp_results.drop(columns = cols_to_drop, axis=1)

    uemp_states = uemp_results.copy()
    uemp_states = uemp_states.dropna()
    
    id_to_state = unemp_df['title'].str.replace('Unemployment Rate in ','').to_dict()
    uemp_states.columns = [id_to_state[c] for c in uemp_states.columns]
    line_chart = px.line(uemp_states)
    line_chart.show()
    
def unemployee_horizontal_bar():
    unemp_df = fred.search('unemployment rate state', filter=('frequency','Monthly'))
    unemp_df = unemp_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')
    unemp_df = unemp_df.loc[unemp_df['title'].str.contains('Unemployment Rate')]
    all_results = []

    for myid in unemp_df.index:
        print("unemp_df.index: ", myid)
        results = fred.get_series(myid)
        results = results.to_frame(name=myid)
        all_results.append(results)
        time.sleep(0.1) # Don't request to fast and get blocked
    uemp_results = pd.concat(all_results, axis=1)

    cols_to_drop = []
    for i in uemp_results:
        print("uemp_result: ", i)
        if len(i) > 4:
            cols_to_drop.append(i)
    uemp_results = uemp_results.drop(columns = cols_to_drop, axis=1)

    uemp_states = uemp_results.copy()
    uemp_states = uemp_states.dropna()
    
    ax = uemp_states.loc[uemp_states.index == '2020-05-01'].T \
        .sort_values('2020-05-01') \
        .plot(kind='barh', figsize=(8, 12), width=0.7, edgecolor='black',
            title='Unemployment Rate by State, May 2020')
    ax.legend().remove()
    ax.set_xlabel('% Unemployed')
    plt.show()