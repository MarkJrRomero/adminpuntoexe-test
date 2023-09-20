var table = $('#tabla-productos').DataTable({
  responsive: true,
  serverSide: true,
  searchable: false,
  orderCellsTop: true,
  sAjaxSource: urlTablaProductos,
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
      { data: 1, name: 'desc' },
      { data: 2, name: 'ref' },
      { data: 3, name: 'prov' },
      {
        name: "cos_uni",
        data: null,
        render: function (data) {
          return formatoPesoColombiano(data[4]);
        },
      },
  ],
  order: [[0, 'desc']]
})

