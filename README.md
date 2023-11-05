
# Forward Options

Very simple code, put here as a reference and archive.

Dynamics under risk free neutral measure:

- dS = S*(r*dt + sigma*dW)
- dB = r*B*dt

sigma and r are constants.
Then we have D(t,T) = P(t,T) = exp(-r*(T-t))

Finally the forward price is G(t,T) = S(t)/P(t,T)

Payoffs for forward calls/puts use S(T) and G(0,T)
