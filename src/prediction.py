import pandas as pd
import numpy as np

def custom_prediction(model, prediction):
    print("\nCUSTOM DIAMOND PRICE PREDICTION")

    try:

        carat = float(input("Enter carat weight: "))
        cut = input("Enter cut (Fair, Good, Very Good, Premium, Ideal): ")
        color = input("Enter color (D, E, F, G, H, I, J): ").upper()
        clarity = input("Enter clarity (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF): ").upper()

        depth = float(input("Enter depth percentage: "))
        table = float(input("Enter table percentage: "))
        x = float(input("Enter length (x): "))
        y = float(input("Enter width (y): "))
        z = float(input("Enter depth (z): "))

        if carat <= 0:
            raise ValueError("Carat must be greater than zero.")

        if depth <= 0:
            raise ValueError("Depth must be greater than zero.")

        if table <= 0:
            raise ValueError("Table must be greater than zero.")

        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError("Diamond dimensions must be greater than zero.")

        valid_cut = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
        valid_color = ["D", "E", "F", "G", "H", "I", "J"]
        valid_clarity = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

        if cut not in valid_cut:
            raise ValueError("Invalid cut.")

        if color not in valid_color:
            raise ValueError("Invalid color.")

        if clarity not in valid_clarity:
            raise ValueError("Invalid clarity.")

        user_diamond = pd.DataFrame({

            "carat": [carat],
            "cut": [cut],
            "color": [color],
            "clarity": [clarity],
            "depth": [depth],
            "table": [table],
            "x": [x],
            "y": [y],
            "z": [z]

        })

        print("\nDIAMOND INFORMATION")

        diamond_summary = pd.DataFrame({
            "Value": [
                carat,
                cut,
                color,
                clarity,
                depth,
                table,
                x,
                y,
                z
            ]
        },
        index=[
            "carat",
            "cut",
            "color",
            "clarity",
            "depth",
            "table",
            "length (x)",
            "width (y)",
            "depth (z)"
        ])

        print(diamond_summary)

        log_prediction = model.predict(user_diamond)[0]
        prediction = np.expm1(log_prediction)

        print("\nDIAMOND INFORMATION")
        print(f"Carat   : {carat}")
        print(f"Cut     : {cut}")
        print(f"Color   : {color}")
        print(f"Clarity : {clarity}")
        print(f"Depth   : {depth}")
        print(f"Table   : {table}")
        print(f"x        : {x}")
        print(f"y        : {y}")
        print(f"z        : {z}")

        print(f"\nEstimated Diamond Price: ${prediction:,.2f}")

    except ValueError as error:
        print("\nInvalid input:", error)