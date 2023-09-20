var table = $('#tabla-inventario').DataTable({
  responsive: true,
  serverSide: true,
  searchable: false,
  orderCellsTop: true,
  sAjaxSource: urlTablaInventario,
  language: {
      decimal: "",
      emptyTable: "No hay información",
      info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
      infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
      infoFiltered: "(Filtrado de _MAX_ total entradas)",
      infoPostFix: "",
      thousands: ",",
      lengthMenu: "Mostrar _MENU_ Entradas",
      loadingRecords: "Cargando...",
      processing: "Procesando...",
      search: "Buscar:",
      zeroRecords: "Sin resultados encontrados",
      paginate: {
        first: "Primero",
        last: "Ultimo",
        next: "Siguiente",
        previous: "Anterior",
      },
    },
  columns: [
      { data: 0, name: 'id' },
      {
        name: "producto",
        data: null,
        render: function (data) {
          return data[1] + " - " + data[2] 
        },
      },
      { data: 3, name: 'cantidad' }
  ],
  order: [[0, 'desc']],
})

