import pandas as pd
from recommender.utils import get_defillama_data

df = pd.read_csv("./defillama_protocols_clean.csv")

def recommend(input_text):
    input_text = input_text.strip().lower()
    results = []

    for _, row in df.iterrows():
        name = row["name"].lower()
        category = row.get("category", "").lower()
        chain = row.get("chain", "")
        url = row.get("url", "")

        if input_text in name or input_text in category:
            enrich = get_defillama_data(name)
            tvl = enrich.get('tvl', 'N/A')
            token = enrich.get('token', 'N/A')
            price = enrich.get('price', 'N/A')

            enriched_text = f"""<b>{row['name']}</b> ({chain})<br>
<ul>
  <li><b>TVL:</b> ${tvl:,}</li>
  <li><b>Token:</b> {token}</li>
  <li><b>Price:</b> ${price}</li>
  <li><a href="{url}" target="_blank">Website</a></li>
</ul>"""
            results.append(enriched_text)

    return "<hr>".join(results[:5]) if results else "No protocols matched your query."
