load('data.mat'); % value: data

sectors = {'Technical work', 'Security/housekeeping/other', 'Insurance', 'Engineering/machinery/energy', 'Electronics/appliances/semiconductor/instrumentation', 'Construction/infrastructure/gardening', 'Computer hardware'};

origin_raw_hash = containers.Map(sectors, {
31, 45, 28, 12, 10, 24, 5
});

ARIMA_predicts_hash = containers.Map(sectors, {
    Technicalwork, Security, Insurance, Engineering, ElectronicApplicance, Construction, computerhf 
});

for sector = sectors
    sector = sector{1};
    train_and_plot(ARIMA_predicts_hash(sector), data, origin_raw_hash(sector), sector);
end