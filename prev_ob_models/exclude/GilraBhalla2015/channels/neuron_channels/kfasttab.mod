TITLE HH fast potassium channel with FUCNTION_TABLEs
: Hodgkin - Huxley potassium channel with parameters from fitting curves to
: the data given in US Bhalla and JM Bower, J. Neurophysiol. 69:1948-1983
: (1993)
: Adapted from /usr/local/neuron/demo/release/nachan.mod - squid
: by Andrew Davison, The Babraham Institute.

NEURON {
	SUFFIX K2_mit_usb
	USEION k READ ek WRITE ik
	RANGE gkbar, ik
	GLOBAL ninf, kinf, ntau, ktau
}

UNITS {
	(mA) = (milliamp)
	(mV) = (millivolt)
}

INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}
PARAMETER {
	v (mV)
	dt (ms)
	gkbar= 0.120 (mho/cm2) <0,1e9>
	ek = -70 (mV)
}
STATE {
	n k
}
ASSIGNED {
	ik (mA/cm2)
	ninf
	kinf
	ntau (ms)
	ktau (ms)
}

INITIAL {
	rates(v)
	n = ninf
	k = kinf
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	ik = gkbar*n*n*k*(v - ek)
}

DERIVATIVE states {
	rates(v)
	n' = (ninf - n)/ntau
	k' = (kinf - k)/ktau
}

FUNCTION_TABLE tabninf(v(mV))
FUNCTION_TABLE tabntau(v(mV)) (ms)
FUNCTION_TABLE tabkinf(v(mV))
FUNCTION_TABLE tabktau(v(mV)) (ms)

PROCEDURE rates(v(mV)) {
	ninf = tabninf(v)
	ntau = tabntau(v) 
	kinf = tabkinf(v)
	ktau = tabktau(v)
}
