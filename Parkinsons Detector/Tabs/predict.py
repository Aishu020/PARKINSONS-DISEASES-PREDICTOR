"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of Parkinson's disease.
            </p>
        """, unsafe_allow_html=True)
    with st.expander("View attribute details"):
        st.markdown("""MDVP:Fo(Hz) - Average vocal fundamental frequency\n
MDVP:Fhi(Hz) - Maximum vocal fundamental frequency\n
MDVP:Flo(Hz) - Minimum vocal fundamental frequency\n
MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several
measures of variation in fundamental frequency\n
MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude\n
NHR,HNR - Two measures of ratio of noise to tonal components in the voice\n
status - Health status of the subject (one) - Parkinson's, (zero) - healthy\n
RPDE,D2 - Two nonlinear dynamical complexity measures\n
DFA - Signal fractal scaling exponent\n
spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation""")
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    avff = st.slider("Average vocal fundamental frequency", int(df["AVFF"].min()), int(df["AVFF"].max()))
    mavff = st.slider("Maximum vocal fundamental frequency", int(df["MAVFF"].min()), int(df["MAVFF"].max()))
    mivff = st.slider("Minimum vocal fundamental frequency", int(df["MIVFF"].min()), int(df["MIVFF"].max()))
    jitddp = st.slider("Jitter:DDP", float(df["Jitter:DDP"].min()), float(df["Jitter:DDP"].max()))
    mdvpjit = st.slider("Multidimensional Voice Program:Jitter(%)", float(df["MDVP:Jitter(%)"].min()), float(df["MDVP:Jitter(%)"].max()))
    mdvprap = st.slider("MDVP:RAP", float(df["MDVP:RAP"].min()), float(df["MDVP:RAP"].max()))
    mdvpapq = st.slider("MDVP:APQ", float(df["MDVP:APQ"].min()), float(df["MDVP:APQ"].max()))
    mdvpppq = st.slider("MDVP:PPQ", float(df["MDVP:PPQ"].min()), float(df["MDVP:PPQ"].max()))
    mdvpshim = st.slider("MDVP:Shimmer", float(df["MDVP:Shimmer"].min()), float(df["MDVP:Shimmer"].max()))
    shimdda = st.slider("Shimmer:DDA", float(df["Shimmer:DDA"].min()), float(df["Shimmer:DDA"].max()))
    shimapq3 = st.slider("Shimmer:APQ3", float(df["Shimmer:APQ3"].min()), float(df["Shimmer:APQ3"].max()))
    shimapq5 = st.slider("Shimmer:APQ5", float(df["Shimmer:APQ5"].min()), float(df["Shimmer:APQ5"].max()))
    nhr = st.slider("NHR", float(df["NHR"].min()), float(df["NHR"].max()))
    hnr = st.slider("HNR", float(df["HNR"].min()), float(df["HNR"].max()))
    rpde = st.slider("RPDE", float(df["RPDE"].min()), float(df["RPDE"].max()))
    dfa = st.slider("DFA", float(df["DFA"].min()), float(df["DFA"].max()))
    d2 = st.slider("D2", float(df["D2"].min()), float(df["D2"].max()))
    ppe = st.slider("PPE", float(df["PPE"].min()), float(df["PPE"].max()))

    # Create a list to store all the features
    features = [avff, mavff, mivff, jitddp, mdvpjit, mdvprap,mdvpapq,mdvpppq,mdvpshim,shimdda,shimapq3,shimapq5,nhr,hnr,rpde,dfa,d2,ppe]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.success("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person either has Parkison's disease or prone to get Parkinson's disease")
        else:
            st.info("The person is safe from Parkinson's disease")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
