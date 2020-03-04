from sklearn.preprocessing import LabelEncoder

def convert(data, columns):
    number=LabelEncoder()
    d = data.copy()
    for c in columns:
        d[c] = number.fit_transform(d[c])
    return d