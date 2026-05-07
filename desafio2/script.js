document.addEventListener('DOMContentLoaded', () => {
    const roomButtons = document.querySelectorAll('.room-btn');
    const timeGrid = document.getElementById('time-grid');
    const reserveBtn = document.getElementById('reserve-btn');
    const messageEl = document.getElementById('message');
    const bookedList = document.getElementById('booked-list');

    // Armazenamento das reservas
    const reservations = {
        'Sala A': [],
        'Sala B': [],
        'Sala C': []
    };

    let selectedRoom = 'Sala A';
    let selectedTime = null;

    // Blocos de hora
    const timeSlots = [];
    for (let i = 8; i <= 17; i++) {
        const start = i.toString().padStart(2, '0') + ':00';
        const end = (i + 1).toString().padStart(2, '0') + ':00';
        timeSlots.push(`${start} - ${end}`);
    }

    function renderTimeSlots() {
        timeGrid.innerHTML = '';
        selectedTime = null;
        updateReserveButton();

        timeSlots.forEach(slot => {
            const btn = document.createElement('button');
            btn.className = 'time-btn';
            btn.textContent = slot;

            const isBooked = reservations[selectedRoom].includes(slot);

            if (isBooked) {
                btn.classList.add('booked');
                btn.disabled = true;
                btn.setAttribute('aria-label', `Horário ${slot} indisponível`);
            } else {
                btn.setAttribute('aria-label', `Selecionar horário ${slot}`);
                btn.addEventListener('click', () => selectTime(slot, btn));
            }

            timeGrid.appendChild(btn);
        });
    }

    function selectTime(slot, btn) {
        document.querySelectorAll('.time-btn').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
        selectedTime = slot;
        updateReserveButton();
        hideMessage();
    }

    function updateReserveButton() {
        reserveBtn.disabled = !selectedTime;
    }

    function showMessage(text, type) {
        messageEl.textContent = text;
        messageEl.className = `message ${type}`;

        setTimeout(() => {
            hideMessage();
        }, 3000);
    }

    function hideMessage() {
        messageEl.className = 'message hidden';
    }

    function updateBookedList() {
        let allReservations = [];
        for (const [room, times] of Object.entries(reservations)) {
            times.forEach(time => {
                allReservations.push({ room, time });
            });
        }

        // Ordena por sala e depois por horário
        allReservations.sort((a, b) => {
            if (a.room !== b.room) return a.room.localeCompare(b.room);
            return a.time.localeCompare(b.time);
        });

        if (allReservations.length === 0) {
            bookedList.innerHTML = '<li class="empty-state">Nenhuma reserva feita.</li>';
            return;
        }

        bookedList.innerHTML = '';
        allReservations.forEach(res => {
            const li = document.createElement('li');
            li.innerHTML = `
                <div><span class="badge-room">${res.room}</span><span class="time-text">${res.time}</span></div>
                <div class="delete-icon" data-room="${res.room}" data-time="${res.time}"></div>
            `;
            bookedList.appendChild(li);
        });

        // Adiciona event listeners aos ícones de exclusão
        document.querySelectorAll('.delete-icon').forEach(icon => {
            icon.addEventListener('click', (e) => {
                const room = e.target.dataset.room;
                const time = e.target.dataset.time;

                // Remover reserva
                reservations[room] = reservations[room].filter(t => t !== time);

                // Renderizar componentes
                renderTimeSlots();
                updateBookedList();

                showMessage('Reserva cancelada com sucesso!', 'success');
            });
        });
    }

    // Event Listeners
    roomButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            roomButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            selectedRoom = btn.dataset.room;
            renderTimeSlots();
            hideMessage();
        });
    });

    reserveBtn.addEventListener('click', () => {
        if (!selectedTime) return;

        // Checagem de reserva duplicada
        if (reservations[selectedRoom].includes(selectedTime)) {
            showMessage('Horário já reservado!', 'error');
            return;
        }

        // Adiciona reserva
        reservations[selectedRoom].push(selectedTime);
        const bookedTime = selectedTime;

        // Renderiza
        renderTimeSlots();
        updateBookedList();

        // Mostra sucesso
        showMessage(`Reserva confirmada: ${selectedRoom} às ${bookedTime}`, 'success');
    });

    // Inicializa
    renderTimeSlots();
});
