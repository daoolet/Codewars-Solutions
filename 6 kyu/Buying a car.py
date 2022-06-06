def nbMonths(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    #print(start_price_old, start_price_new, saving_per_month, percent_loss_by_month)
    month = 0
    saving = saving_per_month

    if start_price_old - start_price_new >= 0:
        return [month, start_price_old - start_price_new]

    while True:
        start_price_old -= start_price_old*percent_loss_by_month/100
        start_price_new -= start_price_new*percent_loss_by_month/100
        month += 1
        
        if start_price_old - start_price_new + saving >= 0:
            return [month, round(start_price_old - start_price_new + saving)]

        saving += saving_per_month

        if month%2 == 0:
            percent_loss_by_month += 0
        else:
            percent_loss_by_month += 0.5