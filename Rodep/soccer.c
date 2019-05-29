void user_main(void)
{
    int n1,n2,n3,n4;
    while (TRUE) {
        if (gAD[CN2] > 204) {
            while (gAD[CN2] > 204) {
                for (n1 = 0; n1 < 1; n1++) {
                    motor(-60, -40);
                    wait_ms(100);
                }
                for (n2 = 0; n2 < 1; n2++) {
                    motor(-40, -40);
                    wait_ms(200);
                }
            }
        } else {
            if (gAD[CN1] > 10) {
                motor(50, 50);
            } else {
                while (gAD[CN2] < 20) {
                    for (n3 = 0; n3 < 1; n3++) {
                        motor(-30, 100);
                        wait_ms(100);
                    }
                    for (n4 = 0; n4 < 1; n4++) {
                        motor(100, -30);
                        wait_ms(100);
                    }
                }