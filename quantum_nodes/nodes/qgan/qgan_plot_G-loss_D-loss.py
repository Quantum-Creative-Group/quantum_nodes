# Plot progress w.r.t the generator's and the discriminator's loss function
# -------------------- WIP

# t_steps = np.arange(num_epochs)
# plt.figure(figsize=(6, 5))
# plt.title("Progress in the loss function")
# plt.plot(
#     t_steps, qgan.g_loss, label="Generator loss function", color="mediumvioletred", linewidth=2
# )
# plt.plot(
#     t_steps, qgan.d_loss, label="Discriminator loss function", color="rebeccapurple", linewidth=2
# )
# plt.grid()
# plt.legend(loc="best")
# plt.xlabel("time steps")
# plt.ylabel("loss")
# plt.show()