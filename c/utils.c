
int is_prime(int n) {
    if (n < 2) { 
        return 0;
    }
    
    int i = 2;
    for (i; i < n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
    
}
