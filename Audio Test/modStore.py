def discrete_FT(signal, N):
    "This function performs the N-point DFT on signal"
    
    import warnings
    from math import pi
    from math import sqrt
    import cmath
    
    # Checking data length
    sigLen = len(signal)
    if sigLen > N:        
        N = sigLen
        warnings.warn('N is smaller than signal length. Assign N = signal length.')        
    elif sigLen < N:
        buffer = signal        
        # Zero padding
        for i in range(N-sigLen):
            buffer.append(0)
            
    # Performing DFT         
    output = []
    for k in range(N):
        buf = 0
        for n in range(N):  
            buf = buf + signal[n]*cmath.exp(-1j*2*pi*n*k/N)
        buf = buf*sqrt(N)
        
        output.append(buf)
              
    return output        
            
            
            
            
            
            
            
            
            
            
            
            
                
               
        