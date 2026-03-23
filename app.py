# Format for a native share intent
share_text = "Check out my tasks!"
share_url = f"intent:#Intent;action=android.intent.action.SEND;type=text/plain;S.android.intent.extra.TEXT={share_text};end"

st.markdown(f'<a href="{share_url}" style="text-decoration:none;"><button style="width:100%;">📤 Share to AI Apps</button></a>', unsafe_allow_html=True)
