#Importing the libraries
import numpy as np
import pickle
import streamlit as st

#loading the saved model
model = pickle.load(open("/home/miki/Desktop/Miki/customer-churning-analysis/models/result.pkl", 'rb'))

#Creating a function for Prediction
def main():
    st.title("Customer Churn Prediction")
    # changing the input data to a numpy array
    cons_12m = st.text_input("Electricity consumption for 12 month")
    cons_gas_12m = st.text_input("Gas consumption for 12 month")
    cons_last_month = st.text_input("Electricity consumption of last month")
    forecast_cons_12m = st.text_input("Forcasted electricity consumption of the next 12 month")
    forecast_discount_energy = st.text_input("Forcasted discount energy")
    forecast_meter_rent_12m = st.text_input("Forcasted meters rent")
    forecast_price_energy_off_peak = st.text_input("Forcasted price energy for first month")
    forecast_price_energy_peak = st.text_input("jk")
    forecast_price_pow_off_peak = st.text_input("ty")
    has_gas = st.text_input("gasd")
    imp_cons = st.text_input("hyt")
    margin_gross_pow_ele = st.text_input("nm")
    margin_net_pow_ele = st.text_input("hg")
    nb_prod_act = st.text_input("df")
    net_margin = st.text_input("kjh")
    pow_max = st.text_input("bng")
    tenure = st.text_input("dfs")
    months_activ = st.text_input("kjhs")
    months_to_end = st.text_input("a")
    months_modif_prod = st.text_input("q")
    months_renewal = st.text_input("p")
    channel_epu = st.text_input("x")
    channel_ewp = st.text_input("v")
    channel_fix = st.text_input("fiyu")
    channel_foo = st.text_input("l")
    channel_lmk = st.text_input("asd")
    channel_sdd = st.text_input("lkjh")
    channel_usi = st.text_input("mnb")
    origin_ewx = st.text_input("lkjgfd")
    origin_kam = st.text_input("vsdg")
    origin_ldk = st.text_input("pok")
    origin_lxi = st.text_input("vdfsd")
    origin_usa = st.text_input("vsdxcd")
    price_off_peak_var = st.text_input("bnvffd")
    price_peak_var = st.text_input("Price of energy for the 1st period (off peak)")
    price_mid_peak_var = st.text_input("Price of energy for the 3rd period (mid peak)")
    price_off_peak_fix = st.text_input("Price of power for the 1st period (off peak)")
    price_peak_fix = st.text_input("Price of power for the 2nd period (peak)")
    price_mid_peak_fix = st.text_input("Price of power for the 3rd period (mid peak)")
    if st.button("Predict"):
        input_features = np.array([cons_12m, cons_gas_12m, cons_last_month, forecast_cons_12m, forecast_discount_energy, forecast_meter_rent_12m, forecast_price_energy_off_peak, forecast_price_energy_peak,
 forecast_price_pow_off_peak, has_gas, imp_cons, margin_gross_pow_ele, margin_net_pow_ele,
 nb_prod_act,net_margin,pow_max, tenure,months_activ,months_to_end,months_modif_prod,
 months_renewal,channel_epu, channel_ewp,channel_fix,channel_foo,channel_lmk,channel_sdd,
 channel_usi,origin_ewx,origin_kam,origin_ldk,origin_lxi,origin_usa,price_off_peak_var,
 price_peak_var,price_mid_peak_var,price_off_peak_fix,price_peak_fix, price_mid_peak_fix], dtype=object)
        prediction = model.predict([input_features])
        output = round(prediction[0], 2)
        if output == 0:
            st.success(f"Your Customer is Not Churned")
        else:

            st.success(f"Your Customer is Churned")
if __name__ == '__main__':
    main()


 

