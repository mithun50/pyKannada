#calculator.py

ಎ = ಪೂರ್ಣಸಂಖ್ಯೆ(ಒಳಸೇರಿಸು('ಮೊದಲ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ: '))
ಬ = ಪೂರ್ಣಸಂಖ್ಯೆ(ಒಳಸೇರಿಸು('ಎರಡನೇ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ: '))
ಚಲನ = ಒಳಸೇರಿಸು('ಚಲನ ( +, -, *, /, **) ನಮೂದಿಸಿ: ')


ಕಾರ್ಯ ಎಣಿಕೆ(ಎ, ಬ, ಚಲನ):
    ಒಂದು_ವೇಳೆ ಚಲನ == '+':
        ಮುದ್ರಿಸು(ಎ + ಬ)
    ಇಲ್ಲದಿದ್ದರೆ ಚಲನ == '-':
        ಮುದ್ರಿಸು(ಎ - ಬ)
    ಇಲ್ಲದಿದ್ದರೆ ಚಲನ == '*':
        ಮುದ್ರಿಸು(ಎ * ಬ)
    ಇಲ್ಲದಿದ್ದರೆ ಚಲನ == '/':
        ಮುದ್ರಿಸು(ಎ / ಬ)
    ಇಲ್ಲದಿದ್ದರೆ ಚಲನ == '**' :
        ಮುದ್ರಿಸು(ಎ ** ಬ)
    ಬೇರೆ:
        ಮುದ್ರಿಸು('ತಪ್ಪು ಚಲನ')




ಎಣಿಕೆ(ಎ, ಬ, ಚಲನ)