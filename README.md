# homework-2

## Autoreg
- 00_LSTM: three LSTM layers (50 units each) + dropout (0.2 each), scores 9.5369
- 01_BiLSTM: three Bidirectional LSTM layers (256 units each) + dropout (0.2 each), scores 4.0945
- 02_GRU: three GRU layers (256 units each) + dropout (0.2 each), similar to 00_LSTM, not submitted
- 03_BiGRU: three Bidirectional GRU layers (256 units each) + dropout (0.2 each), scores 8.2179
- 04_BiLSTM: four Bidirectional LSTM layers (256 units each) + dropout (0.2 each), scores 5.0126
- 05_BiLSTM: two Bidirectional LSTM layers (256 units each) + dropout (0.2 each), scores 5.1252
- 06_seq2seq: 3enc+2dec BiLSTM layers (256 units each), waiting for test
- 07_seq2seq-attention: 3enc+2dec BiLSTM layers (256 units each) + attention mechanism, waiting for test

## Oneshot
- 00_LSTM: three LSTM layers (50 units each) + dropout (0.2 each), similar to its autoreg counterpart, not submitted
- 01_BiLSTM: three Bidirectional LSTM layers (256 units each) + dropout (0.2 each), scores 6.5361
- 02_BiGRU: three Bidirectional LSTM layers (256 units each) + dropout (0.2 each), scores 5.1881
