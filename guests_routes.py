from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Guest

guests_bp = Blueprint('guests', __name__)

@guests_bp.route('/guests', methods=['GET', 'POST'])
def guests():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        side = request.form.get('side', '').strip()
        amount = request.form.get('amount', '').strip()
        note = request.form.get('note', '').strip()

        if not name or not side or not amount:
            flash('이름, 소속, 금액은 필수입니다.', 'danger')
        else:
            try:
                amount_value = int(amount)
                new_guest = Guest(name=name, side=side, amount=amount_value, note=note)
                db.session.add(new_guest)
                db.session.commit()
                flash('축의금이 추가되었습니다.', 'success')
                return redirect(url_for('guests.guests'))
            except ValueError:
                flash('금액은 숫자로 입력해주세요.', 'danger')

    search_name = request.args.get('search_name', '').strip()
    base_query = Guest.query
    if search_name:
        base_query = base_query.filter(Guest.name.contains(search_name))

    groom_guests = base_query.filter(Guest.side == 'groom').order_by(Guest.id.desc()).all()
    bride_guests = base_query.filter(Guest.side == 'bride').order_by(Guest.id.desc()).all()

    groom_total = sum(g.amount for g in groom_guests)
    bride_total = sum(b.amount for b in bride_guests)

    return render_template(
        'guests.html',
        groom_guests=groom_guests,
        bride_guests=bride_guests,
        groom_total=groom_total,
        bride_total=bride_total,
        search_name=search_name
    )


@guests_bp.route('/guests/<int:guest_id>/delete', methods=['POST'])
def delete_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    db.session.delete(guest)
    db.session.commit()
    flash('축의금 항목이 삭제되었습니다.', 'info')
    return redirect(url_for('guests.guests'))
