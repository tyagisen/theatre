from .models import CustomerSeat
def get_best_seat(theatre, num_seats):
    seats = CustomerSeat.objects.filter(theatre=theatre, is_available =True)
    best_seats = []
    current_row = None
    current_group = []
    for seat in seats:
        if current_row is None or seat.row == current_row+1:
            current_group.append(seat)
            current_row = seat.row
            if len(current_group) == num_seats:
                best_seats.extend(current_group)
                break
        
        else:
            current_row = None
            current_group = []
    return best_seats