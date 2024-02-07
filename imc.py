import streamlit as st

with st.sidebar:
    st.title("Calcular o seu IMC")
    st.header("IMC: O que é?")
    st.write("Índice de Massa Corporal (IMC)")
    st.write("É um cálculo que ajuda a avaliar se a pessoa está dentro do seu peso ideal, de acordo com a altura.")
    st.write("É utilizado como uma medida de saúde geral e para determinar se uma pessoa está em um peso saudável para "
             "a sua altura.")

st.title("Calculadora")

peso = st.number_input(label="Digite o seu peso (kg)", min_value=0.0)
altura = st.number_input(label="Digite a sua altura (m)", min_value=0.0)

if  st.button("Calcular"):
    imc = peso / (altura ** 2)
    imc_ideal = 21.7
    imc_delta = imc - imc_ideal

    if imc < 18.5:
        resultado = {
            "classe": 'Abaixo do peso',
            "delta": imc_delta
        }
    elif 18.5 <= imc < 25:
        resultado = {
            "classe": 'Peso ideal',
            "delta": imc_delta
        }
    elif 25 <= imc <= 30:
        resultado = {
            "classe": 'Sobrepeso',
            "delta": imc_delta
        }
    elif imc <= 40:
        resultado = {
            "classe": 'Obesidade',
            "delta": imc_delta
        }
    else:
        resultado = {
            "classe": 'Obesidade mórbida',
            "delta": imc_delta
        }

    st.code(f"O resultado é {resultado}")

    col1, col2 = st.columns(2)

    col1.metric("Classificação do seu IMC:", resultado["classe"], delta_color="inverse")
    col2.metric("Resultado do seu IMC:", round(imc, 2),delta_color="off")

    st.divider()
    st.text("Fonte")
    

