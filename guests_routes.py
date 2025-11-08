from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import func, case
from models import db, Guest

guests_bp = Blueprint('guests', __name__)

@guests_bp.route('/', methods=['GET', 'POST'])
def list_guests():
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
                return redirect(url_for('guests.list_guests'))
            except ValueError:
                flash('금액은 숫자로 입력해주세요.', 'danger')

    search_name = request.args.get('search_name', '').strip()

    # 각 쿼리를 독립적으로 생성
    groom_query = Guest.query.filter(Guest.side == 'groom')
    bride_query = Guest.query.filter(Guest.side == 'bride')
    totals_query = db.session.query(
        func.coalesce(func.sum(case((Guest.side == 'groom', Guest.amount), else_=0)), 0).label('groom_total'),
        func.coalesce(func.sum(case((Guest.side == 'bride', Guest.amount), else_=0)), 0).label('bride_total')
    )

    if search_name:
        search_filter = Guest.name.contains(search_name)
        groom_query = groom_query.filter(search_filter)
        bride_query = bride_query.filter(search_filter)
        totals_query = totals_query.filter(search_filter)

    groom_guests = groom_query.order_by(Guest.id.desc()).all()
    bride_guests = bride_query.order_by(Guest.id.desc()).all()
    totals = totals_query.first()

    groom_total = totals.groom_total or 0
    bride_total = totals.bride_total or 0


    return render_template(
        'guests.html',
        groom_guests=groom_guests,
        bride_guests=bride_guests,
        groom_total=groom_total,
        bride_total=bride_total,
        search_name=search_name
    )


@guests_bp.route('/<int:guest_id>/delete', methods=['POST'])
def delete_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    db.session.delete(guest)
    db.session.commit()
    flash('축의금 항목이 삭제되었습니다.', 'info')
    return redirect(url_for('guests.list_guests'))
