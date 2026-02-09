import streamlit as st

st.title("🎯 Hello from Streamlit!")
st.write("If you can see this, Streamlit Cloud works in your corporate environment!")

st.success("✅ Test successful!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"👋 Hello, {name}! The app is working!")
```

4. **Click:** "Commit changes"

---

## Step 3: Create requirements.txt

1. **Click:** "Add file" → "Create new file"
2. **Filename:** `requirements.txt`
3. **Paste:**
```
streamlit
